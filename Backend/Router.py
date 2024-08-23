from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Backend import Service, Schemas
from Backend.configs import Database
from Backend.helperUtils.ResponseHelper import SuccessResponse, ErrorResponse

"Author @Arun"
router = APIRouter()


def get_db():
    db = Database.DBSession()
    try:
        yield db
    finally:
        db.close()


@router.post(path="/sign-in", response_model=Schemas.UserSignInResponse)
def user_login(sign_in: Schemas.UserSignIn, db: Session = Depends(get_db)):
    try:
        db_user = Service.access_user(sign_in=sign_in, db=db)
        response = Schemas.UserSignInResponse(
            token="wVYrxaeNa9OxdnULvde1Au5m5w63",
            user={
                "userName": db_user.UserName,
                "email": db_user.UserEmail,
                "avatar": "/img/avatars/thumb-1.jpg",
                "authority": ['admin', 'user']
            },
        )
        print(f"Response:{response}")
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.post(path="/sign-up", response_model=Schemas.UserSignInResponse)
def user_create(sign_up: Schemas.User, db: Session = Depends(get_db)):
    try:
        db_user = Service.create_user(sign_up=sign_up, db=db)
        response = Schemas.UserSignupResponse(
            status=status.HTTP_200_OK,
            statusText="OK"
        )
        print(f"Response:{response}")
        status_code = status.HTTP_200_OK
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.post("/scan-qr", response_model=Schemas.Queue)
def scan_qr(customer: Schemas.CustomerCreate, db: Session = Depends(get_db)):
    try:
        db_customer = Service.create_customer(db=db, customer=customer)
        db_queue = Service.create_queue(db=db, customer_id=db_customer.id)
        status_code = status.HTTP_200_OK
        return db_queue
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.post("/fetch-token", response_model=Schemas.QueueBase)
def fetch_token(db: Session = Depends(get_db)):
    try:
        get_current_token = Service.check_tokens(db=db)
        status_code = status.HTTP_200_OK
        return get_current_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.post("/approve-token/{token_id}")
def approve_token(data: Schemas.TokenSelect, db: Session = Depends(get_db)):
    try:
        update_token = Service.update_approve_tokens(db=db, token_number=data.token_id)
        status_code = status.HTTP_200_OK
        return status_code
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.post("/delete-token/{token_id}")
def delete_token(data: Schemas.TokenSelect, db: Session = Depends(get_db)):
    try:
        update_token = Service.update_served_tokens(db=db, token_number=data.token_id)
        status_code = status.HTTP_200_OK
        return status_code
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


#Dealer Creation(Dealer will be having Multiple shop outlets)
@router.post(path="/create-dealer", response_model=Schemas.Dealer)
def user_login(new_dealer: Schemas.Dealer, db: Session = Depends(get_db)):
    try:
        db_dealer = Service.create_dealer(new_dealer=new_dealer, db=db)
        if db_dealer:
            response = Schemas.Dealer(
                status=status.HTTP_200_OK,
                statusText="OK",
            )
        else:
            response = Schemas.Dealer(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                statusText="Database Not Updated",
            )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.post(path="/update-dealer/", response_model=Schemas.Dealer)
def update_dealer(data: Schemas.Dealer, db: Session = Depends(get_db)):
    try:
        db_dealer = Service.update_dealer(data=data, db=db)
        if db_dealer:
            response = Schemas.Dealer(
                status=status.HTTP_200_OK,
                statusText="OK",
            )
        else:
            response = Schemas.Dealer(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                statusText="Database Not Updated",
            )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.post(path="/create_shop")
def create_shop(new_shop: Schemas.Shop, db: Session = Depends(get_db)):
  #  global boolean success = true
    try:
        db_shop = Service.create_shop(new_shop=new_shop, db=db)
        if db_shop:
            success = SuccessResponse(
                statusCode=status.HTTP_200_OK,
                status="success",
                success=True,
                message="Shop created successfully")
        else:
            success = ErrorResponse(
                statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR,
                status="error",
                message="Database Error Occurred"
            )
        return success
    except Exception as e:
        response = ErrorResponse(
            statusCode=status.HTTP_500_INTERNAL_SERVER_ERROR,
            status="error",
            message=str(e),
            data=None
        )
        return response

