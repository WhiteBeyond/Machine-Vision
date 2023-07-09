#import lib
import cv2
import numpy as np
from PIL import Image
import math
#set img from jpg file
jpg_file=r'lena_.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
HSI = [Image.new(imgPIL.mode, imgPIL.size) for i in range(0, 4)] # array to store new color img

#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------
#Funtion for conv RGB to HSI
for x in range(width):
    for y in range(height):
        #RGB value
        R, G, B  = imgPIL.getpixel((x, y))
        t1 =((R -G ) + (R - B))/2
        t2 = np.sqrt((R - G)*(R - G) + (R - B) *(G - B))
        theta = np.arccos(t1 / t2)
        #H
        if B<=G: 
            H=np.rad2deg(theta)
        else: 
            H=360 - np.rad2deg(theta) 
        #S
        S =( 1 - 3 * min(R, G, B) / (R + G + B) ) * 255 #[0, 255]
        #I
        I = (R + G + B) / 3
        #set pixel to img
        HSI[0].putpixel((x, y), (np.uint8(H), np.uint8(H), np.uint8(H)))
        HSI[1].putpixel((x, y), (np.uint8(S), np.uint8(S), np.uint8(S)))
        HSI[2].putpixel((x, y), (np.uint8(I), np.uint8(I), np.uint8(I)))
        HSI[3].putpixel((x, y), (np.uint8(I), np.uint8(S), np.uint8(H))) #cause BGR instead of RGB
    
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
#cv2.imshow('Lenna', img)
cv2.imshow('HUE channel', np.array(( HSI[0] ))) 
cv2.imshow('Saturation channel', np.array(( HSI[1] )))
cv2.imshow('Intensity channel', np.array(( HSI[2] )))
cv2.imshow('HSI', np.array(( HSI[3] )))
cv2.waitKey()
cv2.destroyAllWindows()
