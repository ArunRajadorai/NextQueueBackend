"""
Module Name: CompanyController.py
Author: Arun
"""
from starlette import status
from Backend.helperUtils.ResponseHelper import ErrorResponse, SuccessResponse
from ..schemaUtils.CompanySchema import CompanyResponse
from ..services.CompanyService import CompanyService  # Adjust import as necessary
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from ..schemaUtils import CompanySchema
from Backend.configs.Database import get_db
from Backend.dao.CompanyDao import CompanyDao

# Initialize router and services
company_router = APIRouter()
company_dao = CompanyDao()
company_service = CompanyService(company_dao)


@company_router.post(path="/create_company")
def create_company(new_company: CompanySchema.CompanyCreate, db: Session = Depends(get_db)):
    try:
        response = company_service.create_company(new_company, db)
        if response:
            return SuccessResponse(statusCode=status.HTTP_200_OK, status="success", message="Shop created successfully")
        else:
            return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                 message="Database Error Occurred")
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@company_router.get(path="/fetch_company")
def fetch_shop(db: Session = Depends(get_db)):
    try:
        response = company_service.get_all_company(db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@company_router.delete(path="/delete_company")
def delete_company(com_id: CompanySchema.CompanyDelete, db: Session = Depends(get_db)):
    try:
        response = company_service.delete_company(com_id, db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))


@company_router.get(path="/companies")
def fetch_shop(db: Session = Depends(get_db)):
    try:
        response = company_service.get_companiesforShop(db)
        return response
    except Exception as e:
        return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message=str(e))
