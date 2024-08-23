"""
Module Name: CompanyService.py
Author: Arun
"""
from sqlalchemy import select, true

from Backend import Model
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import logging

from Backend.dao import CompanyDao
from Backend.dao.ShopDao import ShopDao
from Backend.helperUtils.ResponseHelper import SuccessResponse, ErrorResponse, SuccessShopResponse
from Backend.schemaUtils import ShopSchema
from . import QRCodeService
from ..models.ShopModel import Shop as shop
from ..schemaUtils.ShopSchema import ShopCreate, ShopResponse

logger = logging.getLogger(__name__)


class ShopService:

    def __init__(self, dao: ShopDao, qr_code_service: QRCodeService):
        self.dao = dao
        self.qr_code_service = qr_code_service

    def create_shop(self, new_shop_data: ShopSchema, db: Session):
        try:
            logger.info("Invoking service call")
            db_response = self.dao.create_shop(db, new_shop_data)
            shop_id = db_response.ShopID

            # Generate QR Code
            qr_response = self.qr_code_service.create_qr(shop_id, db)
            result_message = "QR code creation successful" if qr_response else "QR code creation failed"
            logger.info(result_message)

            #Business Logic
            if db_response:
                return SuccessResponse(statusCode=status.HTTP_200_OK, status="success",
                                       message="Shop created successfully")
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Database Error Occurred")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_shops(self, db: Session):
        try:
            logger.info("Getting all shops")
            db_response = self.get_shop_summary(db)
            if db_response:
                return SuccessResponse(statusCode=200, status="success", message="Shops retrieved successfully",
                                       data=db_response)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Error Fetching Data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    #
    def get_shop_summary(self, db: Session):
        try:
            # Query to fetch only the required fields
            query = select(shop.ShopID, shop.ShopName, shop.Town, shop.State, shop.Email)
            result = db.execute(query).fetchall()
            shops = [
                {"id": row[0],
                 "name": row[1],
                 "location": f"{row[2]}, {row[3]}",  # Combine town and state
                 "email": row[4]
                 }
                for row in result
            ]
            return shops
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database error occurred: {str(e)}")

    def delete_shop(self, res_id: ShopSchema.ShopDelete, db):
        try:
            db_response = self.dao.delete_shop(db, res_id.id)
            if db_response:
                return SuccessResponse(statusCode=status.HTTP_200_OK, status="success",
                                       message="Shop deleted successfully")
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Database Error Occurred")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def fetch_oneshop(self, res_id: ShopSchema.ShopDelete, db):
        try:
            db_response = self.dao.getshop_by_id(db, res_id.id)
            if db_response:
                return SuccessShopResponse(ShopData=db_response)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Database Error Occurred")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def find_shop(self, shop_id: int, db):
        try:
            db_response = self.dao.getshop_by_id(db, shop_id)
            if db_response:
                return SuccessResponse(status="success", data=db_response, statusCode=status.HTTP_200_OK, message="Shop found")
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message="Database Error Occurred")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

