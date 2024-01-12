import  cv2 as cv
capt=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*"XVID")
out=cv.VideoWriter("output.avi",fourcc,20,(640,480))
print(capt.isOpened())
capt.set(3,3000)
capt.set(4,3000)
print(capt.get(3))
print(capt.get(4))
while(capt.isOpened()):
    ret,frame=capt.read()
    if ret == True:
        out.write(frame)
        

    cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xFF ==ord("a"):
        break
capt.release()
cv.destroyAllWindows()