from typing import Type, TypeVar, Generic, List, Optional
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Define a generic type variable for the DAO class
T = TypeVar('T', bound='Base')


class BaseDao(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self, db: Session) -> List[T]:
        """Retrieve all records."""
        return db.query(self.model).all()

    def get_by_id(self, db: Session, id: int) -> Optional[T]:
        """Retrieve a record by its ID."""
        return db.query(self.model).filter(self.model.ShopID == id).all()

    def create_shop(self, db: Session, obj_in: BaseModel) -> T:
        """Create a new shop record."""
        obj_data = obj_in.model_dump()
        obj = self.model(**{
            'ShopName': obj_data.get('shopName'),
            'ShopOwnerName': obj_data.get('shopOwnername'),
            'CompanyID': obj_data.get('company'),
            'PhoneNumber': obj_data.get('shopPhone'),
            'Email': obj_data.get('shopEmail'),
            'Address': obj_data.get('shopAddress1'),
            'Address2': obj_data.get('shopAddress2'),
            'Town': obj_data.get('shopTown'),
            'PostalCode': obj_data.get('postalcode'),
            'State': obj_data.get('shopState'),
            'Country': obj_data.get('country')
        })
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database error occurred: {str(e)}")

    def get_company_summary(self, db: Session):
        """Get a summary of companies."""
        try:
            query = select(
                self.model.CompanyID,
                self.model.CompanyName,
                self.model.Town,
                self.model.State,
                self.model.Email
            )
            result = db.execute(query).fetchall()
            shops = [
                {
                    "id": row[0],
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

    def update(self, db: Session, id: int, obj_in: BaseModel) -> Optional[T]:
        """Update an existing record."""
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj:
            for key, value in obj_in.model_dump().items():
                setattr(obj, key, value)
            try:
                db.commit()
                db.refresh(obj)
                return obj
            except SQLAlchemyError as e:
                db.rollback()
                raise Exception(f"Database error occurred: {str(e)}")
        return None

    def delete(self, db: Session, id: int) -> bool:
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

    def count(self, db: Session) -> int:
        """Count the number of records."""
        return db.query(self.model).count()

    def filter(self, db: Session, **filters) -> List[T]:
        """Filter records based on given criteria."""
        query = db.query(self.model)
        for key, value in filters.items():
            query = query.filter(getattr(self.model, key) == value)
        return query.all()

    def get_companies(self, db: Session):
        """Get a list of companies."""
        try:
            query = select(self.model.CompanyID, self.model.CompanyName)
            result = db.execute(query).fetchall()
            companies = [
                {"id": row[0], "name": row[1]}
                for row in result
            ]
            return companies
        except SQLAlchemyError as e:
            db.rollback()
            raise Exception(f"Database error occurred: {str(e)}")
