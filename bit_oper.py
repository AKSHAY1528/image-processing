import numpy as np
import cv2 as cv
def nothing(x):
    pass
cap=cv.VideoCapture(0)
cv.namedWindow("Tracking")
cv.createTrackbar("lH","Tracking",0,255,nothing)
cv.createTrackbar("ls","Tracking",0,255,nothing)
cv.createTrackbar("lv","Tracking",0,255,nothing)
cv.createTrackbar("UH","Tracking",0,255,nothing)
cv.createTrackbar("US","Tracking",0,255,nothing)
cv.createTrackbar("UV","Tracking",0,255,nothing)



while True:
    #frame =cv.imread("image dataset/th.jpg")
    _,frame =cap.read()

    cv.resize(frame,(512,512))
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_h=cv.getTrackbarPos("lH","Tracking")
    l_s=cv.getTrackbarPos("ls","Tracking")
    l_v=cv.getTrackbarPos("lv","Tracking")

    u_h=cv.getTrackbarPos("UH","Tracking")
    u_s=cv.getTrackbarPos("US","Tracking")
    u_v=cv.getTrackbarPos("UV","Tracking")
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    key=cv.waitKey(1)
    if key==27:
        break

cap.release()
cv.destroyAllWindows()