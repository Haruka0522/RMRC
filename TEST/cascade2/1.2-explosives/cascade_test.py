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

images = ['0003_0077_0044_0209_0209.jpg','スクリーンショット_2019-08-10_15-08-27.png','スクリーンショット_2019-08-10_15-09-52.png','スクリーンショット_2019-08-10_15-11-58.png','スクリーンショット_2019-08-10_15-13-23.png','スクリーンショット_2019-08-10_15-14-02.png','スクリーンショット_2019-08-10_15-16-41.png']
if __name__ == '__main__':
    for num,img in enumerate(images):
    	result = detect(img, './cascade/trained_data_V1/cascade.xml')
    	cv.imwrite('V10_result'+str(num)+'.jpg', result)

