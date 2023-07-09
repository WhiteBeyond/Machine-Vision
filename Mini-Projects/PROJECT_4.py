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
#funtion change img on scrolling
def update_image(x):
    threshold = x
    #print(f'threshold: {x}')
    # update grayscale image to binanry
    cv2.imshow('Lenna Grayscale Average', np.array(RGBtoGrayscaleAverage(height, width, Average_img, threshold)))
    cv2.imshow('Lenna Grayscale Lightness', np.array(RGBtoGrayscaleLightness(height, width, Average_img, threshold)))
    cv2.imshow('Lenna Grayscale Luminance', np.array(RGBtoGrayscaleLuminance(height, width, Average_img, threshold)))
#----------------------------------------------------------------------------------------------------    
#Funtion for Average method
def RGBtoGrayscaleAverage(height, width, Average_img, threshold: False):
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            #convert to grayscale using Average medthod
            #gray pixel
            Gray = np.uint8((R+G+B)/3)
            if threshold:
                if Gray < threshold:    Average_img.putpixel((x, y), (0, 0, 0))
                else:   Average_img.putpixel((x, y), (255, 255, 255))
            #set gray pixel to img
            else:
                
            #set gray pixel to img
                Average_img.putpixel((x, y), (Gray, Gray, Gray))
    return Average_img
#----------------------------------------------------------------------------------------------------
#Funtion for Lightness method
def RGBtoGrayscaleLightness(height, width, Lightness_img, threshold: False):
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            #convert to grayscale using Lightness medthod
            #gray pixel
            MAX = max(R, G, B)
            MIN = min(R, G, B)
            Gray = np.uint8((MAX + MIN)/2)
            if threshold:
                if Gray < threshold:    Lightness_img.putpixel((x, y), (0, 0, 0))
                else:   Lightness_img.putpixel((x, y), (255, 255, 255))
            #set gray pixel to img
            else:
            #set gray pixel to img
                Lightness_img.putpixel((x, y), (Gray, Gray, Gray))
    return Lightness_img
#----------------------------------------------------------------------------------------------------


#Funtion for Luminance method
def RGBtoGrayscaleLuminance(height, width, Luminance_img, threshold: False):
    for x in range(width):
        for y in range(height):
            #RGB value
            R, G, B  = imgPIL.getpixel((x, y))
            #convert to grayscale using Luminance medthod
            #gray pixel
            Gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
            if threshold:
                if Gray < threshold:    Luminance_img.putpixel((x, y), (0, 0, 0))
                else:   Luminance_img.putpixel((x, y), (255, 255, 255))
            #set gray pixel to img
            else:
                Luminance_img.putpixel((x, y), (Gray, Gray, Gray))
    return Luminance_img
#----------------------------------------------------------------------------------------------------


#display img
cv2.imshow('Lenna', img)
threshold=False #threshold by default = false for funtions display grayscale image
cv2.imshow('Lenna Grayscale Average', np.array(RGBtoGrayscaleAverage(height, width, Average_img, threshold))) 
cv2.imshow('Lenna Grayscale Lightness', np.array(RGBtoGrayscaleLightness(height, width, Lightness_img, threshold)))
cv2.imshow('Lenna Grayscale Luminance', np.array(RGBtoGrayscaleLuminance(height, width, Luminance_img, threshold)))
#trackbar 
cv2.createTrackbar("Threshold", "Lenna", 0, 255, update_image) 
cv2.waitKey()
cv2.destroyAllWindows()
