#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError


HAZMAT_PLACARDS_PATH = "/home/haruka/catkin_ws/src/rmrc_hazmat/hazmat_label2020/"

MIN_MATCH_RATING = 0.7

OBJECT_QUANTITY_LIMIT = 2

MIN_LIMIT_KP = 30

MIN_HIGHT = 400
MAX_HIGHT = 1200#800
MIN_WIDTH = 400
MAX_WIDTH = 1500#800

detector = cv2.xfeatures2d.SIFT_create()

hazmat_list = []
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-1.3-explosive.png"),"1.3 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-1.4-explosive.png"),"1.4 Explosives"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-1.5-blasting-agent.png"),"1.5 Blasting Agent"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-2-flammable-gas.png"),"Flammable Gas"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-2-poison-gas.png"),"Poison Gas"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-3-flammable-liquid.png"),"Flammable Liquid"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-4-dangerous-when-wet.png"),"Dangerous When Wet"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-4-spontaneously-combustible.png"),"Spontaneously Combustible"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-5.1-oxidizer.png"),"Oxidizer"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-6-infectious-substance.png"),"Infectious Substance"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-6-poison-inhalation-hazard.png"),"Poison Inhalation Hazard"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-6-poison.png"),"Poison"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-7-radioactive-ii.png"),"Radioactive ii"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-7-radioactive-iii.png"),"Radioactive iii"))
hazmat_list.append((cv2.imread(HAZMAT_PLACARDS_PATH+"label-8-corrosive.png"),"Corrosive"))

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

rospy.loginfo("finished setting")


class DetectAndRecognize:
    def __init__(self):
        self.image_pub = rospy.Publisher("hazmat",Image,queue_size=5)
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
            if count > OBJECT_QUANTITY_LIMIT:
                break
            cv_clipped = cv_cam_gray[y:(y+h),x:(x+w)]
            clipped_kp,clipped_des = detector.detectAndCompute(cv_clipped,None)
            ans = []
            for temp_kp,temp_des in kp_des_list:
                good = self.matching(clipped_kp,clipped_des,temp_kp,temp_des)
                ans.append(len(good))
            if max(ans) > MIN_LIMIT_KP:
                what_hazmat = hazmat_list[ans.index(max(ans))][1]
                cv2.putText(cv_result,what_hazmat,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(200,0,0))
            cv2.rectangle(cv_result,(x,y),(x+w,y+h),(0,0,255),7)
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
    ic = DetectAndRecognize()
    rospy.init_node("hazmat_node",anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
        cv2.destoryAllWindows()


if __name__ == '__main__':
    main(sys.argv)

