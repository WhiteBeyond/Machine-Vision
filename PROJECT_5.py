#import lib
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#set img from jpg file
jpg_file=r'bird_small.jpg'
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
#func to cal histogram for grayscale img
def CalHistogramGray(GrayscaleImg):
    #new array to store 256 values from 0-255
    his = np.zeros(256)
    for x in range(width):
        for y in range(height):
            #get gray value in from pixel(x,y)
            gR, gB, gB = GrayscaleImg.getpixel((x, y))
            
            #
            his[gR] += 1
    return his
def CalHistogramRGB(ImgPil):
    #new array to store 256 values from 0-255
    hisRGB = np.zeros((3, 256)) #(3,256) ~ [[],[],[]]
    for x in range(width):
        for y in range(height):
            #get gray value in from pixel(x,y)
            gR, gG, gB = ImgPil.getpixel((x, y))
            
            #
            hisRGB[0][gR] += 1
            hisRGB[1][gG] += 1
            hisRGB[2][gB] += 1
    return hisRGB
#----------------------------------------------------------------------------------------------------
#func histogram graph using matplotlib
def DrawHistogram(his, hisRGB):
    w = 6
    h = 4
    #Gray
    plt.figure('Biểu đồ Histogram ảnh mức xám', figsize=(((w,h))), dpi=100)
    XAxis = np.zeros(256)
    XAxis = np.linspace(0, 256, 256)
    plt.plot(XAxis, his, color='magenta')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm có cùng giá trị mức xám')
    #RGB
    plt.figure('Biểu đồ Histogram ảnh RGB', figsize=(((w,h))), dpi=100)
    XAxis = np.zeros(256)
    XAxis = np.linspace(0, 256, 256)
    plt.plot(XAxis, hisRGB[0], color='red')
    plt.plot(XAxis, hisRGB[1], color='green')
    plt.plot(XAxis, hisRGB[2], color='blue')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá màu RGB')
    plt.ylabel('Số điểm có cùng giá trị màu')
    plt.show()

#----------------------------------------------------------------------------------------------------


#display
cv2.imshow('Origin RGB Small Bird IMG', img)

GrayscaleImg=np.array(RGBtoGrayscaleLuminance(height, width, Luminance_img))
cv2.imshow('Smale Bird Grayscale IMG', GrayscaleImg) #display grayscale img

#Draw Historam graph
his_gray = CalHistogramGray(Luminance_img)
his_RGB  = CalHistogramRGB(imgPIL)  
DrawHistogram(his_gray, his_RGB)



cv2.waitKey()
cv2.destroyAllWindows()