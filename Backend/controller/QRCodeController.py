"""
Module Name: QRCodeController.py
Author: Arun
"""
from io import BytesIO

from fastapi import Depends, APIRouter
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from starlette import status

from Backend.configs.Database import get_db
from Backend.dao import QRDao
from Backend.helperUtils.QRCodeGenerator import QRCodeGenerator
from Backend.helperUtils.ResponseHelper import ErrorResponse
from Backend.services.QRCodeService import QRCodeService

qr_router = APIRouter()
qr_service = QRCodeService(qr_code_generator=QRCodeGenerator(), qr_dao=QRDao)


@qr_router.get("/get_QrData")
def get_qr(db: Session = Depends(get_db)):
    try:
        response = qr_service.get_qr_data(db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))
