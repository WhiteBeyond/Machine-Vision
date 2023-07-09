#import lib
import cv2
import numpy as np
from PIL import Image
#set img from jpg file
jpg_file=r'lena_.jpg'
#  jpg_file=r'bird_small.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
Smoothed = [] # array to store new color img

#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------

for n in [3, 5, 7,9]:
    smooth =Image.new(imgPIL.mode, imgPIL.size)
    for x in range((n-1)//2, width - (n-1)//2):
        for y in range((n-1)//2, height - (n-1)//2):
            #RGB value
            Rs, Gs, Bs  = 0, 0, 0
            for i in range(x - (n-1)//2, x + (n-1)//2 + 1):
                for j in range(y - (n-1)//2, y + (n-1)//2 + 1):
                    R, G, B  = imgPIL.getpixel((i, j))
                    Rs += R
                    Gs += G
                    Bs += B
            # cal avg using 6.6 eqn
            K = n * n
            Rs = int(Rs / K)
            Gs = int(Gs / K)
            Bs = int(Bs / K)
            #set pixel to img
            smooth.putpixel((x, y), (np.uint8(Bs), np.uint8(Gs), np.uint8(Rs)))
    Smoothed.append(smooth)        
 #cause BGR instead of RGB

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
#cv2.imshow('Lenna', img)
cv2.imshow('Mask 3x3', np.array(( Smoothed[0] ))) 
cv2.imshow('Mask 5x5', np.array(( Smoothed[1] )))
cv2.imshow('Mask 7x7', np.array(( Smoothed[2] )))
cv2.imshow('Mask 9x9', np.array(( Smoothed[3] )))
cv2.waitKey()
cv2.destroyAllWindows()

