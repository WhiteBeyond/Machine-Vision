#import cv2 numpy
import cv2
import numpy as np

#set img height width variable 
img = cv2.imread('Lenna.jpg', cv2.IMREAD_COLOR)
height = len(img[0])  
width = len(img[1])

#empty RGB variables
R_img = np.zeros((width, height, 3), np.uint8)
G_img = np.zeros((width, height, 3), np.uint8)
B_img = np.zeros((width, height, 3), np.uint8)
#
for i in range(width):
    for j in range(height):
        #RGB value
        R = img[i, j, 2]
        G = img[i, j, 1]
        B = img[i, j, 0]
        #set pixel with RGB value
        R_img[i, j, 2] = R
        G_img[i, j, 1] = G
        B_img[i, j, 0] = B
        
#display img
cv2.imshow('Lenna', img)
cv2.imshow('Lenna Red', R_img)
cv2.imshow('Lenna Green', G_img)
cv2.imshow('Lenna Blue', B_img)
cv2.waitKey()
cv2.destroyAllWindows()