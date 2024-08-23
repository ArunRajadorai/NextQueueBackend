"""
Module Name: CompanyDao.py
Author: Arun
"""
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Backend/dao/company_dao.py
from Backend.dao.BaseDao import BaseDao
from Backend.models.CompanyModel import Company


class CompanyDao(BaseDao[Company]):
    def __init__(self):
        super().__init__(Company)

    def delete_company(self, db: Session, id: int) -> bool:
            """Delete a record by its ID."""
            try:
                obj = db.query(self.model).filter(self.model.CompanyID == id).first()
                if obj:
                    db.delete(obj)
                    db.commit()
                    return True
            except SQLAlchemyError as e:
                db.rollback()
                raise Exception(f"Database error occurred: {str(e)}")
            return False
