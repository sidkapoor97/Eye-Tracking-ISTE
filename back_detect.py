import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("card_1.jpg")
HAZY_WHITE_MIN = np.array([120,120, 120], np.uint8)
HAZY_WHITE_MAX = np.array([150, 150, 150], np.uint8)

dst = cv2.inRange(img, HAZY_WHITE_MIN, HAZY_WHITE_MAX)
no_blue = cv2.countNonZero(dst)

print('The number of blue pixels is: ' + str(no_blue))
if no_blue>15000:
	print("The background is White")
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
