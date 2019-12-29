# coding: utf-8
# raspicam on jetson nano test
import cv2

GST_STR = 'nvarguscamerasrc \
    ! video/x-raw(memory:NVMM), width=1980, height=1080, format=(string)NV12, framerate=(fraction)3/1 \
    ! nvvidconv ! video/x-raw, width=(int)800, height=(int)600, format=(string)BGRx \
    ! videoconvert \
    ! appsink'
WINDOW_NAME = 'Camera Test'

def main():
    capture = cv2.VideoCapture(GST_STR, cv2.CAP_GSTREAMER)

    while True:
        ret, img = capture.read()
        if ret != True:
            break

        cv2.imshow(WINDOW_NAME, img)

        key = cv2.waitKey(10)
        if key == 27: # ESC
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
