# wide_border_qrcode.py

import segno
data=input("Enter the data or link: ")
qrcode = segno.make_qr(data)
filename= input("Enter the filename to save : ")
qrcode.save(
    filename,
    scale=8,
    border=4,
)