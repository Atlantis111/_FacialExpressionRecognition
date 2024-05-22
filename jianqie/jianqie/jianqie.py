# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
 
imgs = []
os_getcwd=os.getcwd().replace('\\','/')
dbDir = os_getcwd + "/db-before/"
print(os_getcwd)
people = os.listdir(dbDir)
 
 
for index in range(len(people)):
    imgPath=dbDir+people[index]
    print('imgPath:',imgPath)
    img = Image.open(imgPath)
    print(img.format, img.size, img.mode)
    #img.show()
    box1 = (0, 0, 512, 512)  # 设置左、上、右、下的像素
    image1 = img.crop(box1)  # 图像裁剪
    #image1.show()
    image1.save('./db-after/'+people[index])  # 存储裁剪得到的图像
