import cv2 as cv
import numpy as np 
img=cv.imread("image dataset/th.jpg")
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()