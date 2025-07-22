import qrcode
from PIL import Image

logo_link='1.png'


logo=Image.open(logo_link)
basewidth=100
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize),Image.BOX)


qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=5,)
qr.add_data("https://forms.gle/mh3XcU9EVZDeLzHb6")
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")

# set size of QR code
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo,pos)

img.save("qr.png")

