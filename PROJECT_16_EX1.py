#Import Thư Viện
import cv2 as cv #Khai báo thư viện OpenCV
import numpy as np #Thư viện tính toán chuyên dụng dùng cho ma trận
from PIL import Image #Thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh
import matplotlib.pyplot as plt #Thư viện để vẽ biểu đồ

#Khai báo đường dẫn filehinh
filehinh = r'lena_.jpg'

#Đọc ảnh màu dùng thư viện OpenCV được mã hóa thành ma trận 3 chiều 
img = cv.imread(filehinh,cv.IMREAD_COLOR)

#Đọc ảnh màu PIL. Ảnh PIL sẽ dùng để thực hiện các tác vụ tính toán và xử lý
imgPIL = Image.open(filehinh)

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]

# Ảnh Dùng Để Chứa Kết Quả Phân đoạn bằng Histogram
Seg_His_Img = Image.new(imgPIL.mode, imgPIL.size)

#------------------------------------------------------------------------
# Khi thử 1 ngưỡng T thì chia bức ảnh thành 2 vùng chia bức ảnh thành 2 vùng


def ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL):
    luminance = Image.new(imgPIL.mode, imgPIL.size)
    
    #Lấy kích thước của ảnh từ imgPIL
    width = imgPIL.size[0]
    height = imgPIL.size[1]
    
    for x in range(width):
        for y in range(height):
            #Lấy giá trị điểm ảnh tại vị trí (x,y)
            R,G,B = imgPIL.getpixel((x,y))

            gray_luminance = np.uint8(0.2126*R+0.7152*G+0.0722*B)

            #Gán giá trị mức xám cho các ảnh
            luminance.putpixel((x,y),(gray_luminance,gray_luminance,gray_luminance))

    return luminance

def TinhHistogram(HinhXamPIL):
    histogram = np.zeros(256) #Vì có 256 phần tử vì có pixel 0 -->255
    #Lấy kích thước ảnh
    width = HinhXamPIL.size[0]
    height = HinhXamPIL.size[1]

    for x in range(width):
        for y in range(height):
            # Lấy giá trị xám tại điểm (x,y)
            gR,gG,gB = HinhXamPIL.getpixel((x,y))

            #Giá trị gray tính ra cũng chính là phần tử thứ gray
            histogram[gR] = histogram[gR]+ 1

    return histogram

#Vẽ biểu đồ histogram
def VeBieuDoHistogram(his):
     w = 6
     h = 5
     plt.figure('Biểu đồ Histogram ảnh xám',figsize=(((w,h))),dpi=100)
     trucX = np.zeros(256)
     trucX = np.linspace(0,256,256)
     plt.plot(trucX,his,color ='orange')
     plt.title('Biểu đồ Histogram')
     plt.xlabel('Giá trị mức xám')
     plt.ylabel('Số điểm cùng giá trị mức xám')
     plt.show()


def Otsu_Multi_Threshold(imgPILGray):
    
    #Tạo mảng tích lũy
    mG = 0
    VarB = np.zeros((256,256))
    VarB_max = 0
    threshold = np.zeros(2)
    
    #Tinh histogram
    his = TinhHistogram(imgPILGray)

    #Lay kich thuoc cua anh tu imgPILGray
    width = imgPILGray.size[0]
    height = imgPILGray.size[1]

    #Tính tần số xuất hiện của điểm ảnh với giá trị từ 0 đến 256
    p = his/(width*height)
    
    #Tính tổng tích lũy
    for k1 in range(256):
        for k2 in range(k1, 256):
            P1 = sum(p[i] for i in range(k1))
            P2 = sum(p[i] for i in range(k1+1, k2))
            P3 = sum(p[i] for i in range(k2+1, 256))

            # Nếu giá trị P = 0 thì thoát
            if(P1 == 0 or P2 == 0 or P3 == 0):
                continue

            # Tính giá trị tích lũy trung bình của các khoảng
            m1 = sum(i*p[i] for i in range(k1))/P1
            m2 = sum(i*p[i] for i in range(k1, k2))/P2
            m3 = sum(i*p[i] for i in range(k2, 256))/P3
            
            #Tính trung bình tích lũy toàn cục mG
            mG = sum(i*p[i] for i in range(256))
            
            #Tính giá trị phương sai toàn cục
            VarG = sum(p[i]*((i - mG)**2) for i in range(256))
            
            #Tính giá trị phương sai giữa 3 miền
            VarB = P1*(m1 - mG)**2 + P2*(m2 - mG)**2 + P3*(m3 - mG)**2
            
            #Lấy 2 giá trị ngưỡng có sự sao cho độ chênh lệch giữa 3 miền lớn nhất
            if VarB > VarB_max:
                VarB_max = VarB
                threshold[0] = k1
                threshold[1] = k2
            
            #Đánh giá độ chính xác
            n = VarB_max/VarG
    print(n)
    return threshold

def Img_Segment(imgPIL, threshold):
    #Make a copy of imgPIL to return the converted image
    img = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = img.size[0]
    height = img.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #calculate the grayscale
            gray = np.uint8(0.2126*r + 0.7152*g + 0.0722*b)
            #Identify the segment value
            if (gray < threshold[0]):
                #Assign the 255 value for image
                img.putpixel((x, y), (0, 0, 0))
            if(gray > threshold[0] and gray < threshold[1]):
                #Assign the 255 value for image
                img.putpixel((x, y), (100, 100, 100))
            if(gray > threshold[0] and gray > threshold[1]):
                #Assign the RGB value for image
                img.putpixel((x, y), (255, 255, 255))
    pic = np.array(img)
    return pic


Anh_Xam = ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL)
threshold = Otsu_Multi_Threshold(Anh_Xam)
print(threshold[0])
print(threshold[1])

Final_img = Img_Segment(Anh_Xam, threshold)

#Histogram Calculation
hisPIL = TinhHistogram(Anh_Xam)


Anh_Xam = np.array(Anh_Xam)      

#Show Image
cv.imshow('Original Image', img)
cv.imshow('Luminance Image', Anh_Xam)
cv.imshow('Segment Image', Final_img)
VeBieuDoHistogram(hisPIL)


#Bấm phím bất kì để đóng cửa sổ
cv.waitKey()
#Quit key
cv.destroyAllWindows()