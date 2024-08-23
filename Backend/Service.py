from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import Model, Schemas
import logging

"Author @Arun"

logging.basicConfig(level=logging.ERROR)  # Configure logging to capture ERROR level and above

logger = logging.getLogger(__name__)


def access_user(sign_in: Schemas.UserSignIn, db: Session):
    try:
        db_user = db.query(Model.User).filter(Model.User.UserName == sign_in.userName).first()
        logger.info("In check User and making db request")
        if db_user:
            if db_user.UserPassword == sign_in.password:
                return db_user
            else:
                raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


def create_user(sign_up: Schemas.User, db: Session):
    logger.info("Create User")
    try:
        db_user = Model.User(UserName=sign_up.username, UserPassword=sign_up.password, UserEmail=sign_up.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        if db.commit():
            return {"message": "User created successfully"}
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


def get_customer(db: Session, customer_id: int):
    return db.query(Model.Customer).filter(Model.Customer.id == customer_id).first()


def create_customer(db: Session, customer: Schemas.CustomerCreate):
    try:
        db_customer = Model.Customer(phoneNumber=customer.phoneNumber)
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of error
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


def create_queue(db: Session, customer_id: int):
    try:
        db_queue = Model.Queue(CustomerID=customer_id)
        db.add(db_queue)
        db.commit()
        db.refresh(db_queue)
        return db_queue
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


def check_tokens(db):
    try:
        return db.query(Model.Queue).filter(Model.Queue.status == Model.StatusEnum.waiting).order_by(
            Model.Queue.Entry_time).first()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Unable to fetch Tokens: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


#Change order status to approved-Green so that person will come and collect
def update_approve_tokens(db, token_number):
    try:
        db_token = db.query(Model.Queue).filter(Model.Queue.Token_number == token_number).first()
        if db_token:
            db_token.status = Model.StatusEnum.approved
            db.commit()
            return db_token
        else:
            raise ValueError("Token ID not found")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Unable to update Tokens: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


#Change order status to served and delete/reset the token
def update_served_tokens(db, token_number):
    try:
        db_token = db.query(Model.Queue).filter(Model.Queue.Token_number == token_number).first()
        if db_token:
            db_token.status = Model.StatusEnum.served
            db.commit()
            return db_token
        else:
            raise ValueError("Token ID not found")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Unable to update Tokens: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")


def create_dealer(new_dealer, db):
    try:
        db_dealers = Model.Dealers(DealerName=new_dealer.name, DealerPhone=new_dealer.phoneNumber,
                                   DealerEmail=new_dealer.email)
        db.add(db_dealers)
        db.commit()
        db.refresh(db_dealers)
        return db_dealers
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Database error occurred")


def create_shop(new_shop, db):
    try:
        db_shop = Model.Shop(ShopName=new_shop.shopName,
                             ShopOwnerName=new_shop.shopOwnername,
                             PhoneNumber=new_shop.shopPhone,
                             Email=new_shop.shopEmail,
                             Address=new_shop.shopAddress1,
                             Address2=new_shop.shopAddress2,
                             Town=new_shop.shopTown,
                             State=new_shop.shopState,
                             PostalCode=new_shop.shopPostalcode,
                             Country=new_shop.country,


                             )
        db.add(db_shop)
        db.commit()
        db.refresh(db_shop)
        return db_shop
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Database error occurred")


def update_dealer(dealer: Schemas.DealerUpdate, db):
    try:
        db_dealer = db.query(Model.Dealers).filter(Model.Dealers.DealerID == dealer.DealerID).first()
        if db_dealer:
            update_data = dealer.dict(exclude_unset=True)  # Only update provided fields
            for key, value in update_data.items():
                if value is not None:
                    db_dealer[key] = value
                    db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Database error occurred")
