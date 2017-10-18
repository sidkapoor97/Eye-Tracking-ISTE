import cv2
import numpy as np

img_rgb = cv2.imread('temp.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

rows,cols,channels=img_rgb.shape

template = cv2.imread('card_1.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6

loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
    print(pt)
    # cv2.imwrite('card')

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', rows,cols)
cv2.imshow('image',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()