import pyqrcode
import png
from pyqrcode import QRCode

r = "https://rahulsinghgaur.github.io/Portfolio/"
# r = "I am Rahul Gaur"
url = pyqrcode.create(r)
url.png("linkQRCode.png",scale = 6)
