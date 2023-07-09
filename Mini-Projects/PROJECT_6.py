#import lib
import cv2
import numpy as np
from PIL import Image

#set img from jpg file
jpg_file=r'Lenna.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
#new CMYK img
'''
cyan_img = Image.new(imgPIL.mode, imgPIL.size)
magenta_img = Image.new(imgPIL.mode, imgPIL.size)
yellow_img = Image.new(imgPIL.mode, imgPIL.size)
black_img = Image.new(imgPIL.mode, imgPIL.size)
# List to store CMYK img
CMYK=[]
CMYK.append(cyan_img)
CMYK.append(magenta_img)
CMYK.append(yellow_img)
CMYK.append(black_img)
'''
CMYK = [Image.new(imgPIL.mode, imgPIL.size) for i in range(0, 4)] #CMYK list to store new color img

#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------
#Funtion for conv RGB to CMYK
def RGBtoCMYK(height, width, CMYK): #CMYK = [[cyan], [magenta], [yellow], [black]]
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            K = min(R, G, B)

            #set pixel to img
            CMYK[0].putpixel((x, y), (B, G, 0))
            CMYK[1].putpixel((x, y), (B, 0, R))
            CMYK[2].putpixel((x, y), (0, G, R))
            CMYK[3].putpixel((x, y), (K, K, K))
    return CMYK
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
cv2.imshow('Lenna', img)
cv2.imshow('Cyan', np.array(( RGBtoCMYK(height, width, CMYK)[0]))) 
cv2.imshow('Magenta', np.array((RGBtoCMYK(height, width, CMYK)[1])))
cv2.imshow('Yellow', np.array((RGBtoCMYK(height, width, CMYK)[2])))
cv2.imshow('Black', np.array((RGBtoCMYK(height, width, CMYK)[3])))
cv2.waitKey()
cv2.destroyAllWindows()
