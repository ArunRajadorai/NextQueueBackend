"""
Module Name: TokenController.py
Author: Arun
"""
import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.logger import logger
from sqlalchemy.orm import Session, sessionmaker
from starlette.websockets import WebSocket, WebSocketDisconnect
from ..configs.Database import get_db, engine
from ..dao.TokenDao import TokenDao
from ..helperUtils.ResponseHelper import ErrorResponse, SuccessResponse
from ..schemaUtils.CustomerSchema import CustomerCreate
from ..schemaUtils.TokenSchema import TokenStatistics, TokenResponse, TokenCreationResponse, UpdateTokenStatus
from ..services.TokenService import TokenService
from starlette import status
import json
import asyncio

token_router = APIRouter()

token_service = TokenService(dao=TokenDao())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@token_router.post(path="/update_token")
def update_token(status_update: UpdateTokenStatus, db: Session = Depends(get_db)):
    try:
        response = token_service.update_token(status_update, db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


#Admin Tool Fetches Token
@token_router.websocket("/ws/fetch_token")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            db = SessionLocal()
            message_type, data = await websocket.receive()
            data = await websocket.receive_text()

            request_data = json.loads(data)
            shop_id = request_data.get("shop_id")

            stats = token_service.get_all_tokens(db, shop_id)
            # Convert the response to JSON and send it
            json_data = stats.json()  # Serialize to JSON string
            await websocket.send_text(json_data)
            #await websocket.send_json(stats.dict())  # Assuming stats is a Pydantic model
            await asyncio.sleep(1)  # Send updates every 5 seconds, adjust as needed
            db.close()
    except WebSocketDisconnect:
        print("Fetch Token client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close(code=1002)


#Customer devices makes connection with nextQueue server in order to get Status Update
@token_router.websocket("/ws/customer_token")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:

            message_type, data = await websocket.receive()
            data = await websocket.receive_text()
            try:
                db = SessionLocal()
                # Parse the incoming message
                request_data = json.loads(data)
                token_number = request_data.get("token")
                shop_id = request_data.get("shop_id")

                if not token_number:
                    await websocket.send_text(json.dumps({"error": "Token number is missing"}))
                    continue

                # Fetch the customer token stats
                stats = token_service.get_customerToken(token_number, shop_id, db)

                # Serialize the response to JSON and send it
                json_data = stats.json()  # Assuming stats is a Pydantic model
                await websocket.send_text(json_data)

                # Sleep to simulate periodic updates
                await asyncio.sleep(5)
                db.close()
            except json.JSONDecodeError:
                await websocket.send_text(json.dumps({"error": "Invalid JSON format"}))
            except Exception as e:
                await websocket.send_text(json.dumps({"error": str(e)}))
                break
    except WebSocketDisconnect:
        print("Customer Token client disconnected")
    except RuntimeError as e:
        print(f"WebSocket error: {e}")


@token_router.post(path="/create_token", response_model=SuccessResponse)
def fetch_token(customer_create: CustomerCreate, db: Session = Depends(get_db)):
    logger.info("Getting all shops")
    try:
        response = token_service.create_customertoken(customer_create, db)
        if response:
            return SuccessResponse(statusCode=200, status="success", message="Token created successfully",
                                   data=response)
        else:
            return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                 message="Error creating token")
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


#From Customer Device to generate new token
@token_router.post(path="/create_customertoken", response_model=SuccessResponse)
def get_token(customer_create: CustomerCreate, db: Session = Depends(get_db)):
    try:
        response = token_service.create_customertoken(customer_create, db)
        if response:
            #token_id_response = TokenCreationResponse(id=response.id)
            return SuccessResponse(statusCode=200, status="success", message="Token created successfully",
                                   data=response)
        else:
            return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                 message="Error creating token")
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@token_router.get(path="/statistics")
def fetch_token(db: Session = Depends(get_db)):
    try:
        response = token_service.get_token_statistics(db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


# WebSocket endpoint for real-time token statistics
@token_router.websocket("/ws/token/statistics")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    db = SessionLocal()
    try:
        while True:
            stats = token_service.get_token_statistics(db)
            await websocket.send_json(stats.dict())  # Assuming stats is a Pydantic model
            await asyncio.sleep(1)  # Send updates every 5 seconds, adjust as needed
            db.close()
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close(code=1002)
