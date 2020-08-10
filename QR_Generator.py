import pyqrcode as qr
import cv2 as cv
from pyqrcode import QRCode
import validators

def input_validation():
    Web_url=input("Enter Your URL:")
    valid=validators.url(Web_url)
    if valid==True:
        print("Valid")
        link = qr.create(Web_url)
        link.png('qr_code.png', scale=8)
        img = cv.imread('qr_code.png', 0)
        cv.imshow('qr_code.png', img)
        cv.waitKey(0)
    else:
        print("Your input was Invalid")
        exit()
input_validation()
