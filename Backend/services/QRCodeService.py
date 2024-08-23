import os
from fastapi import HTTPException
from fastapi.logger import logger
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from starlette import status

from Backend.dao import QRDao
from Backend.helperUtils import QRCodeGenerator
from Backend.helperUtils.ResponseHelper import SuccessResponse, ErrorResponse
from Backend.models.QRModel import QR
from Backend.models.ShopModel import Shop


class QRCodeService:

    def __init__(self, qr_code_generator: QRCodeGenerator, qr_dao=QRDao):
        self.qr_code_generator = qr_code_generator
        self.qr_dao = qr_dao

    def create_qr(self, shop_id: int, db: Session) -> bool:
        try:

            # Generate QR Code
            data = "https://adsecurity.co.uk/"
            img_stream = self.qr_code_generator.generate_qr_code(data)
            #Change QR Backend Path Accordingly
            qr_code_path = f"static/qr_codes/{shop_id}.png"

            # Ensure the directory exists
            os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)

            # Save QR Code to file
            with open(qr_code_path, 'wb') as f:
                f.write(img_stream.read())

            # Update the database with the QR code path
            QRDao.update_qr_path(shop_id, qr_code_path, db)

            return True
        except ValueError as ve:
            print(f"Validation error: {ve}")
            raise HTTPException(status_code=400, detail=str(ve))
        except IOError as e:
            print(f"Error saving QR code file: {e}")
            raise HTTPException(status_code=500, detail="Error saving QR code file")
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="An unexpected error occurred")

    def get_qr_data(self, db):
        try:
            logger.info("Getting all shops")
            db_response = self.get_qr_summary(db)
            if db_response:
                return SuccessResponse(statusCode=200, status="success", message="Shops retrieved successfully", data=db_response)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message="Error Fetching Data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    #Get QR Page Details
    @staticmethod
    def get_qr_summary(db: Session):
        try:
            # Query to fetch only the required fields
            query = (select(Shop.ShopID, Shop.ShopName, Shop.ShopOwnerName, Shop.Town,
                            Shop.State, Shop.Email, QR.Qr_code, func.date(QR.CreatedAt)).join(QR, Shop.ShopID == QR.ShopID))
            result = db.execute(query).fetchall()

            qr_data = [
                {"id": row[0],
                 "name": row[1],
                 "img": "/img/thumbs/solana.png",
                 "company": "ADS Security Solutions",
                 "manager": row[2],
                 "location": f"{row[3]}, {row[4]}",  # Combine town and state
                 "email": row[5],
                 "qr_code": row[6],
                 "qr_date": row[7]
                 }
                for row in result
            ]
            return qr_data
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database error occurred: {str(e)}")
