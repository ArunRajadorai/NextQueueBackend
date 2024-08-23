"""
Module Name: CompanyDao.py
Author: Arun
"""
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Backend/dao/company_dao.py
from Backend.dao.BaseDao import BaseDao
from Backend.models.ShopModel import Shop
from Backend.schemaUtils.ShopSchema import ShopResponse, ShopCreate


class ShopDao(BaseDao[Shop]):
    def __init__(self):
        super().__init__(Shop)

    def delete_shop(self, db: Session, id: int) -> bool:
        """Delete a record by its ID."""
        try:
            obj = db.query(self.model).filter(self.model.ShopID == id).first()
            # query = select(Shop.ShopID, Shop.ShopName).where(Shop.ShopID == id)
            # obj = db.execute(query).first()
            if obj:
                db.delete(obj)
                db.commit()
                return True
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database error occurred: {str(e)}")
        return False

    def getshop_by_id(self, db: Session, id: int):
        """Retrieve a record by its ID."""
        obj = db.query(self.model).filter(self.model.ShopID == id).first()
#        ShopCreate.from_orm(obj)
        shop_create = ShopCreate(
            shopName=obj.ShopName,
            shopOwnername=obj.ShopOwnerName,
            shopAddress1=obj.Address,
            shopAddress2=obj.Address2,
            shopTown=obj.Town,
            shopState=obj.State,
            country=obj.Country,
            shopPostalcode=obj.PostalCode,
            shopEmail=obj.Email,
            shopPhone=obj.PhoneNumber,
            company=obj.CompanyID
        )
        return shop_create
        #return ShopResponse.model_validate(obj)
