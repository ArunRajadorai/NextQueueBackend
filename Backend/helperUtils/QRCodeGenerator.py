import os

import qrcode

from io import BytesIO
from PIL import Image


class QRCodeGenerator:
    def __init__(self, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4):
        self.version = version
        self.error_correction = error_correction
        self.box_size = box_size
        self.border = border

    def generate_qr_code(self, data: str) -> BytesIO:

        try:
            qr = qrcode.QRCode(
                version=self.version,
                error_correction=self.error_correction,
                box_size=self.box_size,
                border=self.border,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img_stream = BytesIO()
            img.save(img_stream, format='PNG')
            #Update as wanted
            # qr_code_path = f"Backend/staticfiles/qr_codes/"
            # os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
            # img.save(qr_code_path)
            img_stream.seek(0)
            return img_stream
        # return {"url": f"/staticfiles/qr_codes/{shop_name}.png"}
        except Exception as e:
            # Log the error message
            print(f"Error generating QR code: {e}")
            raise
