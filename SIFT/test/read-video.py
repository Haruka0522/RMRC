import cv2
video = cv2.VideoCapture(-1)
while (video.isOpened()):
    ret,frame = video.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

