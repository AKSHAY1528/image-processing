import cv2 as cv
img = cv.imread("C:/opencv/image dataset-20231107T142729Z-001/image dataset/test/kirmixi_test/kirmizi 464.jpg")
cv.imshow("seed",img)
cv.waitKey(0)

## reading vediio
#capture= cv.VideoCapture("C:/opencv/image dataset-20231107T142729Z-001/VID-20180614-WA0056.mp4")
#while True:
    #isTrue, frame=capture.read()
   # cv.imshow("vedio",frame)
  #  if cv.waitKey(20) & 0xFF==ord('d'):
 #       break
#capture.release()
#cv.destroyAllWindows()


## resacling
# def rescale(frame,scale=0.2):
#     width=int(frame.shape[1]*scale)
#     helight=int(frame.shape[0]*scale)
#     dimension=(width,helight)
#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
capture= cv.VideoCapture("C:/opencv/image dataset-20231107T142729Z-001/VID-20180614-WA0056.mp4")
while True:
    isTrue, frame=capture.read()
    frame_resize=rescale(frame)

    cv.imshow("vedio",frame)
    cv.imshow("video resized",frame_resize)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitkey(9)

##DRAWING SHAPES AND TEXT 