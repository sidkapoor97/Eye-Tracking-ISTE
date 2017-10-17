import numpy as np 
import cv2

img=cv2.imread('card_1_f.jpg',cv2.IMREAD_COLOR)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

fgmask = fgbg.apply(img)
fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

cv2.imshow('fgmask',fgmask)
cv2.waitKey(0)
cv2.destroyAllWindows()

