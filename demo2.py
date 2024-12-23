import cv2
from PIL import Image,ImageFilter
import numpy as np
import math
import imutils
import tkinter as tk
from tkinter import Tk, Frame, Label
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog


hinhgoc = cv2.imread('anh6.jpg',1)
img = cv2.resize(hinhgoc, (500, 350))
HinhGocPIL = Image.open('anh6.jpg')
# hinhgoc = cv2.imread(choose,1)
# img = cv2.resize(hinhgoc, (500, 350))
max_size =  10000
min_size = 900
imgHinhGocPIL = HinhGocPIL.resize((500,350))
Width, Height = imgHinhGocPIL.size
# tiền xử lý ảnh (nhận diện đường biên theo phương pháp sobel)
def find_max(a,b,c): 
    max = a
    if max<b : max = b
    if max<c : max = c
    return max
def find_min(a,b,c):
    min = a
    if min>b : min = b
    if min>c : min = c
    return min
# tính mức xám theo pp Lightness (gray = (max(rgb)+min(rgb))/2)
Lightness = imgHinhGocPIL.convert()
for x in range (0, Width):
    for y in range (0, Height):
        r, g, b = imgHinhGocPIL.getpixel((x,y))
        maxgray = find_max(r,g,b);
        mingray = find_min(r,g,b);
        Gray = (int)((maxgray+mingray)/2)
        Lightness.im.putpixel((x,y),(Gray,Gray,Gray))
imgAnhGray=np.array(Lightness)
# tính biên theo phương pháp sobel
Sx = np.array([[-1,-2,-1],
               [ 0, 0, 0],
               [ 1, 2, 1]])
Sy = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])
D0 =200
EdgeSobel=Lightness.convert()
for x in range (1, Width-1):  # quét hết toàn bộ bức ảnh trừ các giá trị sát biên 
    for y in range (1, Height-1):
        XR=0
        YR=0
        for i in range(x-1,x+2):    # dùng 2 vòng for để quét hết 9 điểm xung quanh điểm f(x,y) mình đanh xét 
            for j in range(y-1,y+2):
                r,g,b = Lightness.getpixel((i,j))
                XR += r*Sx[(i-(x-1)),(j-(y-1))]    
                YR += r*Sy[(i-(x-1)),(j-(y-1))] 
                Mag = math.sqrt(XR*XR + YR*YR)
                if Mag <= D0:  
                    Mag = 0
                else:         
                    Mag = 255
                    EdgeSobel.putpixel((x,y),(Mag,Mag,Mag)) #sau khi có được bien độ tiến hành đặt giá trị biên độ này vào điểm ảnh f(x,y) mà chúng ta đang xét đến 
# imgEdgeSobel= np.array(EdgeSobel)
# imgEdgeCanny = cv2.Canny(imgAnhGray,30,200)
# imgHinhGoc = np.array(imgHinhGocPIL)

# cv2.imshow('Hinh anh goc',imgHinhGoc)
# cv2.imshow('Hinh anh gray', imgAnhGray)
# cv2.imshow('Nhan dang duong bien dung phuong phap sobel', imgEdgeSobel)
# cv2.imshow('Nhan dang duong bien dung phuong phap canny', imgEdgeCanny)

# print('finish.....')
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img3 = np.array(EdgeSobel) 
edge = cv2.cvtColor(np.array(img3),cv2.COLOR_BGR2GRAY)
Edge = cv2.Canny(imgAnhGray,30,200)

# tìm các countour trong hình chọn contour lớn nhất có 4 cạnh đủ kích thước
cnts = cv2.findContours(Edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #tính contour ảnh
cnts = imutils.grab_contours(cnts) # xoay ảnh theo đúng vị trí 
cnts = sorted(cnts, key=cv2.contourArea, reverse=True) # sắp xêp thứ tự theo contour giảm dần 

screenCnt = None
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray,100,75,75)

for c in cnts:
    peri = cv2.arcLength(c,True) 
    approx = cv2.approxPolyDP(c, 0.05*peri,True) # tiến hành sấp sỉ giá trị chu vi contour  
    if len(approx) == 4 and max_size > cv2.contourArea(c) > min_size :
        # and max_size > cv2.contourArea(c) > min_size
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
    print("No plate detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1,(0,255,0), 3) 
    mask = np.zeros(gray.shape[:2], dtype=np.uint8) 
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, ) 
    new_image = cv2.bitwise_and(img, img, mask=mask) 
    (x,y) = np.where(mask == 255)
    (topx,topy) = (np.min(x),np.min(y))
    (bottomx,bottomy) = (np.max(x),np.max(y))
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

cv2.imshow('Nhan dang duong bien dung phuong phap sobel', edge)
cv2.imshow('Nhan dang duong bien dung phuong phap canny', Edge)
cv2.imshow('Hinh anh gray',imgAnhGray)
cv2.imshow('Anh goc da duoc ve', img)
cv2.imshow('Anh cat',Cropped)
print('finish.....')
cv2.waitKey(0)
cv2.destroyAllWindows()