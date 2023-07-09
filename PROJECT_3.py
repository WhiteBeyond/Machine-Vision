#import lib
import cv2
import numpy as np
from PIL import Image

#set img from jpg file
jpg_file=r'Lenna.jpg'
img = cv2.imread(jpg_file, cv2.IMREAD_COLOR)

#using PIL lib 
imgPIL = Image.open(jpg_file)
#new gray scale image using average method
Average_img = Image.new(imgPIL.mode, imgPIL.size)
Lightness_img = Image.new(imgPIL.mode, imgPIL.size)
Luminance_img = Image.new(imgPIL.mode, imgPIL.size)
#get height and width
height = imgPIL.height
width = imgPIL.width
#print(f'height:{height} \nwidth:{width}')
#----------------------------------------------------------------------------------------------------
#Funtion for Average method
def RGBtoGrayscaleAverage(height, width, Average_img):
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            #convert to grayscale using Average medthod
            #gray pixel
            Gray = np.uint8((R+G+B)/3)
            #set gray pixel to img
            Average_img.putpixel((x, y), (Gray, Gray, Gray))
    return Average_img
#----------------------------------------------------------------------------------------------------
#Funtion for Lightness method
def RGBtoGrayscaleLightness(height, width, Lightness_img):
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            #convert to grayscale using Lightness medthod
            #gray pixel
            MAX = max(R, G, B)
            MIN = min(R, G, B)
            Gray = np.uint8((MAX + MIN)/2)
            #set gray pixel to img
            Lightness_img.putpixel((x, y), (Gray, Gray, Gray))
    return Lightness_img
#----------------------------------------------------------------------------------------------------
#Funtion for Luminance method
def RGBtoGrayscaleLuminance(height, width, Luminance_img):
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            #convert to grayscale using Luminance medthod
            #gray pixel
            Gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
            #set gray pixel to img
            Luminance_img.putpixel((x, y), (Gray, Gray, Gray))
    return Luminance_img
#----------------------------------------------------------------------------------------------------

#display img
cv2.imshow('Lenna', img)
cv2.imshow('Lenna Grayscale Average', np.array(RGBtoGrayscaleAverage(height, width, Average_img))) 
cv2.imshow('Lenna Grayscale Lightness', np.array(RGBtoGrayscaleLightness(height, width, Lightness_img)))
cv2.imshow('Lenna Grayscale Luminance', np.array(RGBtoGrayscaleLuminance(height, width, Luminance_img)))
cv2.waitKey()
cv2.destroyAllWindows()
