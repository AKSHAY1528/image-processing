import cv2 as cv
import numpy as np 
img1=np.zeros([512,512,3],dtype=np.uint8)
#img=cv.imread("C:/opencv/image dataset-20231107T142729Z-001/image dataset/test/kirmixi_test/kirmizi 464.jpg",1)
#line=cv.line(img,(0,0),(255,255),(255,0,123),thickness=4)
#img=cv.rectangle(img,(384,0),(511,254),(0,255,0),5)ā
#img=cv.circle(img,(420,25),63,(255,26,89),-1)
font=cv.FONT_HERSHEY_COMPLEX
img=cv.putText(img1,"Opencv",(25,100),font,4,(111,111,111),6)
cv.imshow("pic",img1)
cv.waitKey(0)
cv.destroyAllWindows()