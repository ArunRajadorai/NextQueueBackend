"""
Module Name: TokenDao.py
Author: Arun
"""
from fastapi import HTTPException
from fastapi.logger import logger
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from starlette import status

from Backend.dao.BaseDao import BaseDao
from Backend.models.ShopModel import Shop
from Backend.models.TokenModel import Token


class TokenDao(BaseDao[Token]):
    def __init__(self):
        super().__init__(Token)

    @staticmethod
    def get_tokens_by_shop_id(self, shop_id: int, db):
        try:
            return db.query(Token).filter(Token.ShopID == shop_id).all()
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Unable to fetch Tokens: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")

    @staticmethod
    def get_customertoken(token_id, shop_id, db):
        try:
            #db_response = db.query(Token).filter(Token.id == token_id).first()
            db_response = db.query(
                Token.id,
                Token.CustomerID,
                func.to_char(Token.entry_time, 'Mon DD, HH24:MI').label('entry_time'),
                Token.status, Token.token_number,
                Token.ShopID
            ).filter((Token.token_number == token_id) & (Token.ShopID == shop_id)).first()

            if db_response:
                # Convert the result into a dictionary
                token_response = {
                    "tokenNumber": db_response.token_number,
                    "CustomerID": db_response.CustomerID,
                    "dateTime": db_response.entry_time,  # Already formatted
                    "status": db_response.status,
                    "ShopID": db_response.ShopID,
                }
                return token_response
        except SQLAlchemyError as e:
            logger.error(f"Unable to fetch Tokens: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_ERROR, detail="Database error occurred")
