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
threshold=45 
x1=80
y1=400
x2=150
y2=500
S=(x2-x1)*(y2-y1)
Segmented =Image.new(imgPIL.mode, imgPIL.size)
Ra, Ga, Ba  = 0, 0, 0
for i in range(x1 - 1, x2 + 2):
    for j in range(y1 - 1, y2 + 2):
        Rij, Gij, Bij  = imgPIL.getpixel((i, j))
        Ra += Rij
        Ga += Gij
        Ba += Bij
Ra = Ra / S
Ga = Ga / S
Ba = Ba / S

for x in range(width):
    for y in range(height):
        #RGB value
        Rz, Gz, Bz  = imgPIL.getpixel((x, y))
        D = np.sqrt((Rz-Ra)*(Rz-Ra) + (Gz-Ga)*(Gz-Ga) + (Bz-Ba)*(Bz-Ba))
        #set pixel to img
        if D > threshold:
            Segmented.putpixel((x, y), (np.uint8(Bz), np.uint8(Gz), np.uint8(Rz)))
        else:
            Segmented.putpixel((x, y), (np.uint8(255), np.uint8(255), np.uint8(255)))
 #cause BGR instead of RGB

#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#[[][][][]]
#display img
#cv2.imshow('Lenna', img)
cv2.imshow('Segmented Image (threshold:45; x1:80, y1:400, x2:150, y2:500)', np.array((Segmented))) 
cv2.waitKey()
cv2.destroyAllWindows()

