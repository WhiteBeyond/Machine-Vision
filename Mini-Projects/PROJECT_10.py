#import lib
import cv2
import numpy as np
from PIL import Image
#set img from jpg file
jpg_file=r'lena_.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
YCbCr = [Image.new(imgPIL.mode, imgPIL.size) for i in range(0, 4)] # array to store new color img

#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------
#Funtion for conv RGB to XYZ

for x in range(width):
    for y in range(height):
        #RGB value
        R, G, B  = imgPIL.getpixel((x, y))
        Y = 16 + (R*65.738 + G*129.075 + B*25.064)/256
        Cb = 128 - (R*37.495 + G*74.494 - B*112.439)/256
        Cr = 128 + (R*112.439 - G*94.154 - B*18.285)/256
        #set pixel to img
        YCbCr[0].putpixel((x, y), (np.uint8(Y), np.uint8(Y), np.uint8(Y)))
        YCbCr[1].putpixel((x, y), (np.uint8(Cb), np.uint8(Cb), np.uint8(Cb)))
        YCbCr[2].putpixel((x, y), (np.uint8(Cr), np.uint8(Cr), np.uint8(Cr)))
        YCbCr[3].putpixel((x, y), (np.uint8(Cr), np.uint8(Cb), np.uint8(Y))) #cause BGR instead of RGB

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
#cv2.imshow('Lenna', img)
cv2.imshow('Y channel', np.array(( YCbCr[0] ))) 
cv2.imshow('Cb channel', np.array(( YCbCr[1] )))
cv2.imshow('Cr channel', np.array(( YCbCr[2] )))
cv2.imshow('YCbCr Image', np.array(( YCbCr[3] )))
cv2.waitKey()
cv2.destroyAllWindows()

