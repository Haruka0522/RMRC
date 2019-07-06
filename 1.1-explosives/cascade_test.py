import sys
import cv2 as cv

def detect(imagefilename, cascadefilename):
    srcimg = cv.imread(imagefilename)
    if srcimg is None:
        print('cannot load image')
        sys.exit(-1)
    dstimg = srcimg.copy()
    cascade = cv.CascadeClassifier(cascadefilename)
    if cascade.empty():
        print('cannnot load cascade file')
        sys.exit(-1)
    objects = cascade.detectMultiScale(srcimg, 1.1, 3)
    for (x, y, w, h) in objects:
        print(x, y, w, h)
        cv.rectangle(dstimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return dstimg

images = ['1267_0113_0011_0102_0102.jpg','IMG_20190615_070527.jpg','IMG_20190615_071623.jpg','IMG_20190620_163814.jpg']
if __name__ == '__main__':
    for num,img in enumerate(images):
    	result = detect(img, './cascade/trained_data_V9/cascade.xml')
    	cv.imwrite('V9_result'+str(num)+'.jpg', result)

