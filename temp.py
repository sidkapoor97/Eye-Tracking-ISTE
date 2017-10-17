import cv2
import numpy as np 

img=cv2.imread('temp.jpg',cv2.IMREAD_COLOR)

rows,cols,shannels=img.shape
#print(rows,cols)
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', rows,cols)
image=img[140:450,100:300]
cv2.imshow('card_1.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
