import pyqrcode as qr
import cv2 as cv
from pyqrcode import QRCode

Website_Name=input("Enter your website URL:")

link= qr.create(Website_Name)

link.png('qr_code.png',scale=8)

img = cv.imread('qr_code.png',0)
cv.imshow('image',img)
cv.waitKey(0)

