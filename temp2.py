import cv2
import numpy as np 

img=cv2.imread('card_1.jpg',cv2.IMREAD_COLOR)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red=np.array([0,0,0])
upper_red=np.array([100,255	,180])

mask=cv2.inRange(hsv,lower_red,upper_red)
res=cv2.bitwise_and(img,img,mask=mask)

kernel=np.ones((5,5),np.int8)
erosion=cv2.erode(mask,kernel,iterations=1)
dilation=cv2.dilate(mask,kernel,iterations=1)

opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

print(res[40,40])
cv2.imshow('frame',res)
#cv2.imwrite('card_1_f.jpg',res)
cv2.imshow('original',img)
diff=cv2.absdiff(res,img)
cv2.imshow('diff',diff)
cv2.waitKey(0)
cv2.destroyAllWindows()


