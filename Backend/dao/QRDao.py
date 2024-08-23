"""
Module Name: QRDao.py
Author: Arun
"""
from sqlalchemy import text


# Backend/dao/qr_dao.py

class QRDao:

    @staticmethod
    def update_qr_path(shop_id: int, qr_code_path: str, db):
        try:
            # Ensure column names match your schema
            db.execute(
                "UPDATE qrcode SET Qr_code = :qr_code_path, CreatedAt = now() WHERE ShopID = :shop_id",
                {"qr_code_path": qr_code_path, "shop_id": shop_id}
            )
            db.commit()
        except Exception as e:
            print(f"Error updating QR code path in database: {e}")
            db.rollback()
            raise


def update_qr_path(shop_id: int, qr_code_path: str, db):
    try:
        # Use SQLAlchemy's text() to explicitly declare the SQL statement
        sql = text(
            "INSERT INTO qrcode (ShopID, Qr_code, CreatedAt) VALUES (:shop_id, :qr_code_path, now())"
        )
        # Execute the SQL statement with the provided parameters
        # Execute the SQL statement with the provided parameters
        localhost = "http://127.0.0.1:8000/"
        result = db.execute(sql, {"qr_code_path": localhost+qr_code_path, "shop_id": shop_id})

        # Commit the transaction
        db.commit()

    except Exception as e:
        print(f"Error updating QR code path in database: {e}")
        db.rollback()
        raise
