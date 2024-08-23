"""
Module Name: CompanyService.py
Author: Arun
"""
from Backend import Model
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import logging

from Backend.dao import CompanyDao
from Backend.helperUtils.ResponseHelper import SuccessResponse, ErrorResponse
from Backend.schemaUtils import CompanySchema

logger = logging.getLogger(__name__)


class CompanyService:

    def __init__(self, dao: CompanyDao):
        self.dao = dao

    def create_company(self, new_company_data: CompanySchema, db: Session):
        try:
            db_response = self.dao.create(db, new_company_data)
            if db_response:
                return SuccessResponse(statusCode=status.HTTP_200_OK, status="success",message="Company created successfully")
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message="Database Error Occurred")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_company(self, db: Session):
        try:
            logger.info("Getting all Available Companies")
            db_response = self.dao.get_company_summary(db)
            if db_response:
                return SuccessResponse(statusCode=200, status="success", message="Companies retrieved successfully",
                                       data=db_response)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Error Fetching Data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_company(self, com_id: CompanySchema.CompanyDelete, db):
        try:
            db_response = self.dao.delete_company(db, com_id.id)
            if db_response:
                return SuccessResponse(statusCode=status.HTTP_200_OK, status="success", message="Company deleted successfully")
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error", message="Database Error Occurred")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_companiesforShop(self, db):
        try:
            logger.info("Getting all Available Companies")
            company = self.dao.get_companies(db)
            if company:
                return SuccessResponse(statusCode=200, status="success", message="Companies retrieved successfully",
                                       data=company)
            else:
                return ErrorResponse(statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR, status="error",
                                     message="Error Fetching Data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
