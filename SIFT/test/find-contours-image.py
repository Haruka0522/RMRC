import cv2

img = cv2.imread("./IMG_20190615_070527.jpg",0)

#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(img,(11,11),0)
im2 = cv2.threshold(gray,140,240,cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
for pt in cnts:
    x,y,w,h = cv2.boundingRect(pt)
    if w<100 or h<100:
        continue
    print(x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imwrite("test.jpg",img)

