#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError


HAZMAT_PLACARDS_PATH = "/home/haruka/catkin_ws/src/rmrc_hazmat/hazmat-placards/"

MIN_MATCH_RATING = 0.7

QUANTITY_LIMIT = 2

MIN_HIGHT = 400
MAX_HIGHT = 800
MIN_WIDTH = 400
MAX_WIDTH = 800

detector = cv2.xfeatures2d.SIFT_create()

hazmat_list = []
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"1.png"),"1.1 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"2.png"),"1.2 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"3.png"),"1.3 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"4.png"),"1.4 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"5.png"),"1.5 Blasting Agent"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"6.png"),"1.6 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"7.png"),"Flammable Gas"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"8.png"),"Inhalation Hazard 2"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"9.png"),"Non Flammable Gas"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"10.png"),"Oxygen"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"11.png"),"Combustible"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"12.png"),"Flammable"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"13.png"),"Fuel Oil"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"14.png"),"Gasoline"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"15.png"),"Dangerous When Wet"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"16.png"),"Flammable Solid"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"17.png"),"Spontaneously Combustiblle"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"18.png"),"Oxidizer"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"19.png"),"Organic Peroxide"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"20.png"),"Inhalation Hazard 6"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"21.png"),"Poison"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"22.png"),"Toxic"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"23.png"),"Radioactive"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"24.png"),"Corrosive"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"25.png"),"Other Dangerous Goods"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"26.png"),"Dangerous"))

kp1 , des1 = detector.detectAndCompute(hazmat_list[0][0] ,None)
kp2 , des2 = detector.detectAndCompute(hazmat_list[1][0] ,None)
kp3 , des3 = detector.detectAndCompute(hazmat_list[2][0] ,None)
kp4 , des4 = detector.detectAndCompute(hazmat_list[3][0] ,None)
kp5 , des5 = detector.detectAndCompute(hazmat_list[4][0] ,None)
kp6 , des6 = detector.detectAndCompute(hazmat_list[5][0] ,None)
kp7 , des7 = detector.detectAndCompute(hazmat_list[6][0] ,None)
kp8 , des8 = detector.detectAndCompute(hazmat_list[7][0] ,None)
kp9 , des9 = detector.detectAndCompute(hazmat_list[8][0] ,None)
kp10,des10 = detector.detectAndCompute(hazmat_list[9][0] ,None)
kp11,des11 = detector.detectAndCompute(hazmat_list[10][0],None)
kp12,des12 = detector.detectAndCompute(hazmat_list[11][0],None)
kp13,des13 = detector.detectAndCompute(hazmat_list[12][0],None)
kp14,des14 = detector.detectAndCompute(hazmat_list[13][0],None)
kp15,des15 = detector.detectAndCompute(hazmat_list[14][0],None)
kp16,des16 = detector.detectAndCompute(hazmat_list[15][0],None)
kp17,des17 = detector.detectAndCompute(hazmat_list[16][0],None)
kp18,des18 = detector.detectAndCompute(hazmat_list[17][0],None)
kp19,des19 = detector.detectAndCompute(hazmat_list[18][0],None)
kp20,des20 = detector.detectAndCompute(hazmat_list[19][0],None)
kp21,des21 = detector.detectAndCompute(hazmat_list[20][0],None)
kp22,des22 = detector.detectAndCompute(hazmat_list[21][0],None)
kp23,des23 = detector.detectAndCompute(hazmat_list[22][0],None)
kp24,des24 = detector.detectAndCompute(hazmat_list[23][0],None)
kp25,des25 = detector.detectAndCompute(hazmat_list[24][0],None)
kp26,des26 = detector.detectAndCompute(hazmat_list[25][0],None)

kp_des_list = []
kp_des_list.append((kp1 ,des1))
kp_des_list.append((kp2 ,des2))
kp_des_list.append((kp3 ,des3))
kp_des_list.append((kp4 ,des4))
kp_des_list.append((kp5 ,des5))
kp_des_list.append((kp6 ,des6))
kp_des_list.append((kp7 ,des7))
kp_des_list.append((kp8 ,des8))
kp_des_list.append((kp9 ,des9))
kp_des_list.append((kp10,des10))
kp_des_list.append((kp11,des11))
kp_des_list.append((kp12,des12))
kp_des_list.append((kp13,des13))
kp_des_list.append((kp14,des14))
kp_des_list.append((kp15,des15))
kp_des_list.append((kp16,des16))
kp_des_list.append((kp17,des17))
kp_des_list.append((kp18,des18))
kp_des_list.append((kp19,des19))
kp_des_list.append((kp20,des20))
kp_des_list.append((kp21,des21))
kp_des_list.append((kp22,des22))
kp_des_list.append((kp23,des23))
kp_des_list.append((kp24,des24))
kp_des_list.append((kp25,des25))
kp_des_list.append((kp26,des26))

rospy.loginfo("finished setting")


class ClassificateHazmat:
    def __init__(self):
        self.image_pub = rospy.Publisher("hazmat",Image,queue_size=10)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/image_raw",Image,self.callback)

    def callback(self,data):
        #uvc_camからpublishされたものをOpenCVで扱える形式にconvert
        try:
            cv_cam = self.bridge.imgmsg_to_cv2(data,"bgr8")
        except CvBridgeError as e:
            print(e)
        
        """ここから画像に対する処理"""
        cv_cam_gray = cv2.cvtColor(cv_cam,cv2.COLOR_BGR2GRAY)
        cv_cam_gray_blured = cv2.GaussianBlur(cv_cam_gray,(17,17),0)
        cv_cam_binarized = cv2.threshold(cv_cam_gray_blured,0,255,cv2.THRESH_OTSU)[1]
        cv_result = cv_cam.copy()
        cnts = cv2.findContours(cv_cam_binarized,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
        count = 0
        for pt in cnts:
            x,y,w,h = cv2.boundingRect(pt)
            if w < MIN_WIDTH or h < MIN_HIGHT or w > MAX_WIDTH or h > MAX_HIGHT:
                continue
            count += 1
            if count > QUANTITY_LIMIT:
                break
            cv_clipped = cv_cam_gray[y:(y+h),x:(x+w)]
            clipped_kp,clipped_des = detector.detectAndCompute(cv_clipped,None)
            ans = []
            for temp_kp,temp_des in kp_des_list:
                good = self.matching(clipped_kp,clipped_des,temp_kp,temp_des)
                ans.append(len(good))
            what_hazmat = hazmat_list[ans.index(max(ans))][1]
            cv2.rectangle(cv_result,(x,y),(x+w,y+h),(0,0,255),7)
            cv2.putText(cv_result,what_hazmat,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(200,0,0))
        """ここまで画像に対する処理"""

        #OpenCVの形式の画像をROSで扱える形式にconvert
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_result,"bgr8"))
        except CvBridgeError,e:
            print(e)


    def matching(self,camera_kp,camera_des,template_kp,template_des):
        #テストを行って適合したキーポイントを返す
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        #checksは再帰の回数
        search_params = dict(checks = 300)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(template_des, camera_des, k=2)
        good = []
        for m,n in matches:
            if m.distance < MIN_MATCH_RATING*n.distance:
                    good.append(m)
        return good


def main(args):
    ic = ClassificateHazmat()
    rospy.init_node("hazmat_node",anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
        cv2.destoryAllWindows()


if __name__ == '__main__':
    main(sys.argv)

