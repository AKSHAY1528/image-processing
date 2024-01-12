import cv2 as cv
import numpy as np 
#img1=np.zeros([512,512,3],dtype=np.uint8)
img=cv.imread("C:/opencv/image dataset-20231107T142729Z-001/image dataset/test/kirmixi_test/kirmizi 464.jpg",1)
img1=cv.imread("C:/opencv/image dataset-20231107T142729Z-001/image dataset/IMG_0199.JPG",1)
print(img.shape)# returns number of rows and columns ,channels
print(img.size)#pixel of image
print(img.dtype)#image data type
b,e,r=cv.split(img)
img=cv.merge((b,e,r))
ball=img[280:340,330:390]
img[273:333,100:160]=ball
img=cv.resize(img,(512,512))
img1=cv.resize(img1,(512,512))

dst=cv.add(img,img1)
dst2=cv.addWeighted(img,0.5,img1,0.5,0)
cv.imshow("pic",dst2)
cv.waitKey(0)
cv.destroyAllWindows()