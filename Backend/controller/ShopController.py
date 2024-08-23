"""
Module Name: CompanyController.py
Author: Arun
"""
import datetime

from starlette import status
from Backend.helperUtils.ResponseHelper import ErrorResponse
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter

from ..dao import QRDao
from ..helperUtils.QRCodeGenerator import QRCodeGenerator
from ..schemaUtils import ShopSchema
from ..services.QRCodeService import QRCodeService
from ..services.ShopService import ShopService
from Backend.configs.Database import get_db
from ..dao.ShopDao import ShopDao

shop_router = APIRouter()
shop_dao = ShopDao()
shop_service = ShopService(dao=ShopDao(),
                           qr_code_service=QRCodeService(qr_code_generator=QRCodeGenerator(), qr_dao=QRDao))


@shop_router.post(path="/create_shop")
def create_shop(new_shop: ShopSchema.ShopCreate, db: Session = Depends(get_db)):
    try:
        response = shop_service.create_shop(new_shop, db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@shop_router.post("/find_shop")
def find_shop(request: ShopSchema.ShopRequest, db: Session = Depends(get_db)):
    try:
        response = shop_service.find_shop(request.shop_id, db)
        print("Response: ", response, datetime.UTC)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@shop_router.get(path="/fetch_shop")
def fetch_shop(db: Session = Depends(get_db)):
    try:
        response = shop_service.get_all_shops(db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@shop_router.delete(path="/delete_shop")
def delete_shop(res_id: ShopSchema.ShopDelete, db: Session = Depends(get_db)):
    try:
        response = shop_service.delete_shop(res_id, db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@shop_router.post(path="/fetch_editshop")
def fetch_oneshop(res_id: ShopSchema.ShopDelete, db: Session = Depends(get_db)):
    try:
        response = shop_service.fetch_oneshop(res_id, db)
        print(response.ShopData)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))
