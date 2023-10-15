import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("http://lailysfood.blogspot.com/")
qr.make(fit=True)
img=qr.make_image(fill_color='red' , bg_color="blue")
img.save("Lailysfood.png")