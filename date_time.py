import  cv2 as cv
import datetime as dt 
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
        date=str(dt.datetime.now())
        #out.write(frame)
        font=cv.FONT_ITALIC
        text="width:"+str(capt.get(3))+" " + 'height:'+str(capt.get(4))
        cv.putText(frame,date,(10,50),font,1,(0,255,245),2,cv.LINE_AA)
        

    cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xFF ==ord("a"):
        break
capt.release()
cv.destroyAllWindows()