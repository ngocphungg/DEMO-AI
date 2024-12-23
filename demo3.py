import cv2
import imutils
import numpy as пр
from PIL import Image, ImageFilter, ImageTk
import math
import tkinter as tk
from tkinter import Tk, Frame, Label
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
 # Tuj chinh kich thudo cua ánh dau vão
def open_file():
    
    filepath = tk.filedialog.askopenfilename(
        filetypes = [("Text Files","*jpg"), ("All Files","*.*")]
    )
    print(filepath[60:69])
    choose = filepath[60:69]

    max_size =  10000
    min_size = 900
  
    hinhgoc = cv2.imread(choose,1)
    imggoc = Image.open(choose)
    img = cv2.resize(hinhgoc, (500, 350))
    img1 = imggoc.resize((500, 350))
    #ing1 A resized_img.filter(ImageFilter.GaussianBlur(radius=e.8)) # làm mã anh loc bo nhiéu
    Width, Height = img1.size

    Sx = np.array([[-1,-2,-1],
               [ 0, 0, 0],
               [ 1, 2, 1]])
    Sy = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

    D0 =200
    aR=aR=aB=0

    Lightness = img1.convert()
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
    for x in range (1, Width):
        for y in range (1, Height):
            r , g, b = img1.getpixel((x,y))
            maxgray = find_max(r,g,b);
            mingray = find_min(r,g,b);
            Gray = (int)((maxgray+mingray)/2)
            Lightness.im.putpixel((x,y),(Gray,Gray,Gray))
    anhgray= np.array(Lightness)
    Edge = Lightness.convert()
    for x in range (1, Width-1):
        for y in range (1, Height-1):
            XR=0
            YR=0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    r,g,b = Lightness.getpixel((i,j))
                    XR += r*Sx[(i-(x-1)),(j-(y-1))]    
                    YR += r*Sy[(i-(x-1)),(j-(y-1))] 
                    Mag = math.sqrt(XR*XR + YR*YR)
                    if Mag <= D0:
                        Mag = 0
                    else: 
                        Mag = 255
                        Edge.putpixel((x,y),(Mag,Mag,Mag))

