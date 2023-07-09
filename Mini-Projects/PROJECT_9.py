#import lib
import cv2
import numpy as np
from PIL import Image
#set img from jpg file
jpg_file=r'lena_.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
XYZ = [Image.new(imgPIL.mode, imgPIL.size) for i in range(0, 4)] # array to store new color img

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

        X = 0.4124564 * R + 0.3575761 * G + 0.1804375 * B
        Y = 0.2126729 * R + 0.7151522 * G + 0.0721750 * B
        Z = 0.0193339 * R + 0.1191920 * G + 0.9503041 * B
        #set pixel to img
        XYZ[0].putpixel((x, y), (np.uint8(X), np.uint8(X), np.uint8(X)))
        XYZ[1].putpixel((x, y), (np.uint8(Y), np.uint8(Y), np.uint8(Y)))
        XYZ[2].putpixel((x, y), (np.uint8(Z), np.uint8(Z), np.uint8(Z)))
        XYZ[3].putpixel((x, y), (np.uint8(Z), np.uint8(Y), np.uint8(X))) #cause BGR instead of RGB

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
#cv2.imshow('Lenna', img)
cv2.imshow('X channel', np.array(( XYZ[0] ))) 
cv2.imshow('Y channel', np.array(( XYZ[1] )))
cv2.imshow('Z channel', np.array(( XYZ[2] )))
cv2.imshow('XYZ Image', np.array(( XYZ[3] )))
cv2.waitKey()
cv2.destroyAllWindows()


'''
            t1 = np.array([[0.4124564, 0.3575761, 0.1804375],
                        [0.2126729, 0.7151522, 0.0721750],
                        [0.0193339, 0.1191920, 0.9503041]])

            t2 = np.array([[R], [G], [B]])
            #np.matmul(t1,t2) = [[ ], [ ], [ ]]
            X = np.matmul(t1,t2)[0][0]
            Y = np.matmul(t1,t2)[1][0]
            Z = np.matmul(t1,t2)[2][0]
'''
