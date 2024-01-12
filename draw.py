import cv2 as cv
import numpy as np 
blank =np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
# blank[200:300]=0,0,255
# cv.imshow("green",blank)
cv.rectangle(blank,(0,0),((blank.shape[1]//2),(blank.shape[0]//2)),(0,255,0),thickness=2)
cv.imshow("rect",blank)
# img = cv.imread("C:/opencv/image dataset-20231107T142729Z-001/image dataset/test/kirmixi_test/kirmizi 464.jpg")
# cv.circle(blank,(0,25),5)
# cv.imshow("cir",blank)
#cv.imshow('cat',img)
cv.waitKey(0)