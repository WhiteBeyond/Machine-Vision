#Edge Detection - Nhận dạng đường biên dùng phương pháp Sobel cho ảnh mức xám (grayscale image).
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
threshold=130
#grayscale img
Average_img = Image.new(imgPIL.mode, imgPIL.size)
for x in range(width):
    for y in range(height):
        #RGB value
        R, G, B  = imgPIL.getpixel((x, y))
        #convert to grayscale using Average medthod
        #gray pixel
        Gray = np.uint8((R+G+B)/3)
        #set gray pixel to img
        Average_img.putpixel((x, y), (Gray, Gray, Gray))
#edge detect
Array_x = [[ -1, -2, -1 ], [ 0, 0, 0 ], [ 1, 2, 1 ]]
Array_y = [[ -1, 0, 1 ], [ -2, 0, 2 ], [ -1, 0, 1 ]]
EdgeDetected =Image.new(imgPIL.mode, imgPIL.size)

for x in range(1, width - 1):
    for y in range(1, height - 1):
        gx = gy = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                Rij, Gij, Bij = Average_img.getpixel((i,j))
                gx += Rij * Array_x[i-(x-1)][j-(y-1)]
                gy += Rij * Array_y[i-(x-1)][j-(y-1)]
        M = np.abs(gx)+ np.abs(gy)
        if M <= threshold:  EdgeDetected.putpixel((x, y), (0,0,0))
        else:   EdgeDetected.putpixel((x, y), (255,255,255))


#cv2.imshow('Lenna', img)
cv2.imshow('Edge Detected Image (threshold:130)', np.array((EdgeDetected))) 
cv2.waitKey()
cv2.destroyAllWindows()
