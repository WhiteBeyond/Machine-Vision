#import lib
import cv2
import numpy as np
from PIL import Image
#set img from jpg file
jpg_file=r'lena_.jpg'
#jpg_file=r'bird_small.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
#Smoothed = [] # array to store new color img

#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------

Array = [[0,-1,0],[-1,4,-1],[0,-1,0]]
sharpened =Image.new(imgPIL.mode, imgPIL.size)
for x in range(1, width - 1):
    for y in range(1, height - 1):
        #RGB value
        Rs, Gs, Bs  = 0, 0, 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                Rij, Gij, Bij  = imgPIL.getpixel((i, j))
                Rs += Rij * Array[i-(x-1)][j-(y-1)]
                Gs += Gij * Array[i-(x-1)][j-(y-1)]
                Bs += Bij * Array[i-(x-1)][j-(y-1)]
                
        Rxy, Gxy, Bxy  = imgPIL.getpixel((i, j))
        Rs = Rxy + Rs
        Gs = Gxy + Gs
        Bs = Bxy + Bs
        if Rs < 0: Rs = 0
        elif Rs >255: Rs = 255
        if Gs < 0: Gs = 0
        elif Gs >255: Gs = 255
        if Bs < 0: Bs = 0
        elif Bs >255: Bs = 255
        #set pixel to img
        sharpened.putpixel((x, y), (np.uint8(Bs), np.uint8(Gs), np.uint8(Rs)))        
 #cause BGR instead of RGB

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
cv2.imshow('Lenna', img)
cv2.imshow('Sharpened Image', np.array(( sharpened ))) 
cv2.waitKey()
cv2.destroyAllWindows()

