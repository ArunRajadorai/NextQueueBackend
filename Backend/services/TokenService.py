"""
Module Name: TokenService.py
Author: Arun
"""
import datetime

from fastapi import HTTPException
from fastapi.logger import logger
from sqlalchemy import null
from sqlalchemy.sql.functions import now, func
from starlette import status

from Backend.dao.TokenDao import TokenDao
from Backend.helperUtils.ResponseHelper import SuccessResponse, ErrorResponse
from Backend.models.CustomerModel import Customer
from Backend.models.TokenModel import Token, TokenSequence
from Backend.schemaUtils.TokenSchema import TokenResponse, TokenStatistics, UpdateTokenStatus


class TokenService:

    def __init__(self, dao: TokenDao):
        self.dao = dao

    #Passing token id from customer device in order to check the status
    def get_customerToken(self, token_number, shop_id, db):
        try:
            logger.info("Fetching Customer Token")
            db_response = self.dao.get_customertoken(token_number, shop_id, db)
            # db_response = db.query(Token).filter(Token.id == token_number).first()
            #token_responses = TokenResponse.model_validate(db_response)
            # Use the following to get through shop id
            # db_response = self.dao.get_tokens_by_shop_id()
            if db_response:
                return SuccessResponse(statusCode=200, status="success", message="Tokens retrieved successfully",
                                       data=db_response)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Error Fetching Data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_tokens(self, db, shop_id):
        try:
            logger.info("Getting all shops")
            db_response = self.dao.get_by_id(db, shop_id)
            token_responses = [TokenResponse.model_validate(token) for token in db_response]
            #Use the following to get through shop id
            #db_response = self.dao.get_tokens_by_shop_id()
            if db_response:
                return SuccessResponse(statusCode=200, status="success", message="Tokens retrieved successfully",
                                       data=token_responses)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Error Fetching Data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_token_statistics(db):
        try:
            # Count waiting and served tokens & (Token.ShopID == shopId)
            waiting_count = db.query(Token).filter((Token.status == 0)).count()
            served_count = db.query(Token).filter(Token.status == 1).count()

            # Create a TokenStatistics object
            stats = TokenStatistics(
                waiting_tokens=waiting_count,
                served_tokens=served_count,

            )

            return stats
        except Exception as e:
            raise Exception(f"Error fetching token statistics: {str(e)}")

    @staticmethod
    def create_token(db):
        try:
            new_token = Token(CustomerID=1, status=0, ShopID=31)
            db.add(new_token)
            db.commit()
            db.refresh(new_token)
            return new_token
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_customertoken(customer_create, db):
        try:
            # Create and save the new customer
            if customer_create.mobileNumber:  # Check if mobileNumber is not None or empty
                new_customer = Customer(phoneNumber=customer_create.mobileNumber)
                db.add(new_customer)
                db.commit()
                db.refresh(new_customer)
                customer_id = new_customer.CustomerID  # Assign the actual CustomerID
            else:
                customer_id = None

                # Handle token sequence for the shop
            shop_token_sequence = db.query(TokenSequence).filter_by(
                ShopID=customer_create.shopId).with_for_update().first()

            if not shop_token_sequence:
                shop_token_sequence = TokenSequence(ShopID=customer_create.shopId, LastTokenNumber=0)
                db.add(shop_token_sequence)

            # Increment and reset the token number as needed
            shop_token_sequence.LastTokenNumber = (shop_token_sequence.LastTokenNumber % 100) + 1
            shop_token_sequence.last_updated = func.now()

            # Create and save the new token
            new_token = Token(
                CustomerID=customer_id,
                status=0,
                ShopID=customer_create.shopId,
                token_number=shop_token_sequence.LastTokenNumber,
                last_updated=func.now()
            )
            db.add(new_token)
            db.commit()
            db.refresh(new_token)

            # Prepare the response data
            token_response = {
                "id": new_token.id,
                "CustomerID": new_token.CustomerID,
                "entry_time": new_token.entry_time.strftime('%b %d, %H:%M'),
                "status": new_token.status,
                "ShopID": new_token.ShopID,
                "token_number": new_token.token_number
            }
            return token_response

        except Exception as e:
            db.rollback()  # Rollback changes in case of error
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_customertoken1(customer_create, db):
        try:
            new_customer = Customer(phoneNumber=customer_create.mobileNumber)
            db.add(new_customer)
            db.commit()
            db.refresh(new_customer)

            # Create new token for the newly added customer
            new_token = Token(CustomerID=new_customer.CustomerID, status=0, ShopID=customer_create.shopId)
            db.add(new_token)
            db.commit()
            db.refresh(new_token)

            db_response = db.query(
                Token.id,
                Token.CustomerID,
                func.to_char(Token.entry_time, 'Mon DD, HH24:MI').label('entry_time'),
                Token.status,
                Token.ShopID
            ).filter(Token.id == new_token.id).first()

            if db_response:
                # Convert the result into a dictionary
                token_response = {
                    "id": db_response.id,
                    "CustomerID": db_response.CustomerID,
                    "entry_time": db_response.entry_time,  # Already formatted
                    "status": db_response.status,
                    "ShopID": db_response.ShopID,
                }
                return token_response

            return new_token
        except Exception as e:
            db.rollback()  # Rollback changes in case of error
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_token(status_update, db):
        try:
            token = db.query(Token).filter(
                (Token.token_number == status_update.id) & (Token.ShopID == status_update.shop_id)).first()
            if not token:
                raise HTTPException(status_code=404, detail="Token not found")
            if status_update.status == 0:
                token.status = 1
                db.commit()
                db.refresh(token)
                response_data = {
                    "token": token.token_number,
                    "status": token.status
                }
                return SuccessResponse(statusCode=200, status="success", message="Token Updated successfully",
                                       data=response_data)
            else:
                db.delete(token)
                db.commit()
                return SuccessResponse(statusCode=200, status="success", message="Token deleted successfully",
                                       data=token.id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
