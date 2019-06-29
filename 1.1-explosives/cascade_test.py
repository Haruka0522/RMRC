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

if __name__ == '__main__':
    result = detect('neg1714.jpg', './cascade/trained_data_V6/cascade.xml')
    cv.imwrite('V6_result4.jpg', result)

