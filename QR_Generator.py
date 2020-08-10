import pyqrcode as qr
import cv2 as cv
from pyqrcode import QRCode
import validators

def url_validator():
    Website_url=validators.url(input("Enter Your URL:"))
    if Website_url==True:
        link = qr.create(Website_url)

        link.png('qr_code.png', scale=8)

        img = cv.imread('qr_code.png', 0)
        cv.imshow('image', img)
        cv.waitKey(0)
        exit()
    else:
        print("Your input was Invalid")
        url_validator()
url_validator()
