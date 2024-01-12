import numpy as np
import cv2 as cv

#img=cv.imread("C:/opencv/image dataset-20231107T142729Z-001/image dataset/test/kirmixi_test/kirmizi 464.jpg",1)

#events=[i for i in dir(cv) if "EVENT" in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font=cv.FONT_HERSHEY_COMPLEX
        strxy=str(x)+" "+str(y)
        cv.putText(img,strxy,(x,y),font,1,(255,125,98),2)
        cv.imshow("image",img)
img=np.zeros((512,512,3),np.uint8)
cv.imshow("image",img)
cv.setMouseCallback("image",click_event)
cv.waitKey(0)
cv.destroyAllWindows()