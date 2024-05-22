import cv2
import os

person = cv2.imread("img_1693.png")         #将mask图转化为灰度图
mask = cv2.imread("output_1693.png",cv2.IMREAD_GRAYSCALE)       #将人像扣图，使背景部分的像素值为0
mask = mask / 255.0
person[:,:,0] = person[:,:,0] * mask
person[:,:,1] = person[:,:,1] * mask
person[:,:,2] = person[:,:,2] * mask
result = person     #将最终效果图赋值给result
cv2.imwrite("1693.png",result)
