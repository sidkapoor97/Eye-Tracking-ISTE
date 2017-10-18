import cv2
import numpy as np 
import matplotlib.pyplot as plt

img=cv2.imread('temp.jpg',cv2.IMREAD_COLOR)
rows,cols,channels=img.shape
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', cols,rows)
cv2.imshow('image',img)
card=img[845:1157,683:877]
cv2.imshow('image1',card)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv2.imwrite('card_9.jpg',card)




