import pyqrcode
qr="Aravinth"
code=pyqrcode.create(qr)
code.png('Name.png',scale=20)
