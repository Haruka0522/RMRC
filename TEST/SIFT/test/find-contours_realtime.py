import numpy as np
import cv2
import os

GST_STR = 'nvarguscamerasrc \
    ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)30/1 \
    ! nvvidconv ! video/x-raw, width=(int)800, height=(int)600, format=(string)BGRx \
    ! videoconvert \
    ! appsink'

capture = cv2.VideoCapture(GST_STR,cv2.CAP_GSTREAMER)
while True:
    ret,img = capture.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(11,11),0)
    im2 = cv2.threshold(gray,140,240,cv2.THRESH_BINARY_INV)[1]
    cnts = cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
    for pt in cnts:
        x,y,w,h = cv2.boundingRect(pt)
        if w<100 or h<100 or w == 800 or h == 600:
            continue
        print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("test",img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    print(capture.get(cv2.CAP_PROP_FPS))
capture.release()
cv2.destroyAllWindows()
