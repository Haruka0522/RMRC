import os
import cv2

path = "/home/haruka/RMRC/追加neg/"
save_path = "/home/haruka/RMRC/追加neg/"
serial_num = 2000
angle = 135

file_list = os.listdir(path)

if not os.path.exists(save_path):
    os.mkdir(save_path)

def Rotation(src,angle):
    height = src.shape[0]
    width = src.shape[1]
    center = (int(width/2),int(height/2))
    scale = 1.0
    trans = cv2.getRotationMatrix2D(center,angle,scale)
    image2 = cv2.warpAffine(src,trans,(width,height))
    return image2

for file_name in file_list:
    img = cv2.imread(path+"/"+file_name)
    cv2.imwrite(save_path+"/"+str(serial_num)+".jpg",Rotation(img,angle))
    serial_num += 1
