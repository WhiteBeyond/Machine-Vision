##Edge Detection - Nhận dạng đường biên dùng phương pháp Sobel cho ảnh màu RGB
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
#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------
threshold=0
#grayscale img

#edge detect
Array_x = [[ -1, -2, -1 ], [ 0, 0, 0 ], [ 1, 2, 1 ]]
Array_y = [[ -1, 0, 1 ], [ -2, 0, 2 ], [ -1, 0, 1 ]]
EdgeDetected =Image.new(imgPIL.mode, imgPIL.size)

for x in range(1, width - 1):
    for y in range(1, height - 1):
        gxR = gyR = gxG = gyG = gxB = gyB = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                Rij, Gij, Bij = imgPIL.getpixel((i,j))
                gxR += Rij * Array_x[i-(x-1)][j-(y-1)]
                gyR += Rij * Array_y[i-(x-1)][j-(y-1)]
                gxG += Gij * Array_x[i-(x-1)][j-(y-1)]
                gyG += Gij * Array_y[i-(x-1)][j-(y-1)]
                gxB += Bij * Array_x[i-(x-1)][j-(y-1)]
                gyB += Bij * Array_y[i-(x-1)][j-(y-1)]
        gxx = gxR * gxR + gxG * gxG + gxB * gxB
        gyy = gyR * gyR + gyG * gyG + gyB * gyB
        gxy = gxR * gyR + gxG * gyG + gxB * gyB
        theta = np.arctan2(2 * gxy, (gxx - gyy))/2
        F0 = np.sqrt(((gxx + gyy) + (gxx - gyy) * np.cos(2 * theta) + 2 * gxy * np.sin(2 * theta)) / 2)
      
        if F0 <= threshold:  EdgeDetected.putpixel((x, y), (0,0,0))
        else:   EdgeDetected.putpixel((x, y), (255,255,255))

#cv2.imshow('Lenna', img)
cv2.imshow('RGB Edge Detected Image (threshold:130)', np.array((EdgeDetected))) 
cv2.waitKey() 
cv2.destroyAllWindows()