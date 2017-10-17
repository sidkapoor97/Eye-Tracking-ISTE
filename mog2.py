import numpy as np 
import cv2

img=cv2.imread('card_1_f.jpg',cv2.IMREAD_COLOR)

fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold = 10)

fgmask=fgbg.apply(img)

cv2.imshow('mask',fgmask)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()