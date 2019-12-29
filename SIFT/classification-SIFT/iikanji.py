import numpy as np
import cv2
from time import sleep
import os
import matplotlib.pyplot as plt

#----------------------------------------------------
#
#syoki settei
#
#----------------------------------------------------
GST_STR = 'nvarguscamerasrc \
    ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)3/1 \
    ! nvvidconv ! video/x-raw, width=(int)800, height=(int)600, format=(string)BGRx \
    ! videoconvert \
    ! appsink'

placards_path = "./hazmat-placards/"

MIN_MATCH_RATING = 0.6

detector = cv2.xfeatures2d.SIFT_create()

#hazmat_list = [(img1,name1),(img2,name2),...,(img26,name26)]
hazmat_list = []
hazmat_list.append((cv2.imread(placards_path+"1.png"),"1.1 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"2.png"),"1.2 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"3.png"),"1.3 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"4.png"),"1.4 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"5.png"),"1.5 Blasting Agent"))
hazmat_list.append((cv2.imread(placards_path+"6.png"),"1.6 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"7.png"),"Flammable Gas"))
hazmat_list.append((cv2.imread(placards_path+"8.png"),"Inhalation Hazard 2"))
hazmat_list.append((cv2.imread(placards_path+"9.png"),"Non Flammable Gas"))
hazmat_list.append((cv2.imread(placards_path+"10.png"),"Oxygen"))
hazmat_list.append((cv2.imread(placards_path+"11.png"),"Combustible"))
hazmat_list.append((cv2.imread(placards_path+"12.png"),"Flammable"))
hazmat_list.append((cv2.imread(placards_path+"13.png"),"Fuel Oil"))
hazmat_list.append((cv2.imread(placards_path+"14.png"),"Gasoline"))
hazmat_list.append((cv2.imread(placards_path+"15.png"),"Dangerous When Wet"))
hazmat_list.append((cv2.imread(placards_path+"16.png"),"Flammable Solid"))
hazmat_list.append((cv2.imread(placards_path+"17.png"),"Spontaneously Combustible"))
hazmat_list.append((cv2.imread(placards_path+"18.png"),"Oxidizer"))
hazmat_list.append((cv2.imread(placards_path+"19.png"),"Organic Peroxide"))
hazmat_list.append((cv2.imread(placards_path+"20.png"),"Inhalation Hazard 6"))
hazmat_list.append((cv2.imread(placards_path+"21.png"),"Poison"))
hazmat_list.append((cv2.imread(placards_path+"22.png"),"Toxic"))
hazmat_list.append((cv2.imread(placards_path+"23.png"),"Radioactive"))
hazmat_list.append((cv2.imread(placards_path+"24.png"),"Corrosive"))
hazmat_list.append((cv2.imread(placards_path+"25.png"),"Other Dangerous Goods"))
hazmat_list.append((cv2.imread(placards_path+"26.png"),"Dangerous"))

kp1,des1 = detector.detectAndCompute(hazmat_list[0][0],None)
kp2,des2 = detector.detectAndCompute(hazmat_list[1][0],None)
kp3,des3 = detector.detectAndCompute(hazmat_list[2][0],None)
kp4,des4 = detector.detectAndCompute(hazmat_list[3][0],None)
kp5,des5 = detector.detectAndCompute(hazmat_list[4][0],None)
kp6,des6 = detector.detectAndCompute(hazmat_list[5][0],None)
kp7,des7 = detector.detectAndCompute(hazmat_list[6][0],None)
kp8,des8 = detector.detectAndCompute(hazmat_list[7][0],None)
kp9,des9 = detector.detectAndCompute(hazmat_list[8][0],None)
kp10,des10 = detector.detectAndCompute(hazmat_list[9][0],None)
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
kp_des_list.append((kp1,des1))
kp_des_list.append((kp2,des2))
kp_des_list.append((kp3,des3))
kp_des_list.append((kp4,des4))
kp_des_list.append((kp5,des5))
kp_des_list.append((kp6,des6))
kp_des_list.append((kp7,des7))
kp_des_list.append((kp8,des8))
kp_des_list.append((kp9,des9))
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

capture = cv2.VideoCapture(GST_STR,cv2.CAP_GSTREAMER)

#------------------------------------------------------
#
#kansu tachi
#
#------------------------------------------------------
def Matching(camera_kp,camera_des,template_kp,template_des):

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(template_des, camera_des, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
    	if m.distance < MIN_MATCH_RATING*n.distance:
    		good.append(m)

    # return the number of matches (the tutorial describes how to draw the features if interested)
    return good

#------------------------------------------------------
#
#main loop
#
#------------------------------------------------------
while True:
    try:
        cam_ret,cam_img = capture.read()
        if cam_ret != True:
            print("No ret")
            continue
        cam_gray_img = cv2.cvtColor(cam_img,cv2.COLOR_BGR2GRAY)

        '''kakitashi hajimari'''
        cam_gray_img_blured = cv2.GaussianBlur(cam_gray_img,(11,11),0)
        binarized_img = cv2.threshold(cam_gray_img_blured,0,255,cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(binarized_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
        for pt in cnts:
            x,y,w,h = cv2.boundingRect(pt)
            if w<200 or h<200 or w==800 or h==600:
                continue
            clipped_img = cam_gray_img[y:(y+h),x:(x+w)]


            cam_kp,cam_des = detector.detectAndCompute(clipped_img,None)
            ans = []
            for temp_kp,temp_des in kp_des_list:
                good = Matching(cam_kp,cam_des,temp_kp,temp_des)
                ans.append(len(good))
            what_hazmat = hazmat_list[ans.index(max(ans))][1]
            cv2.rectangle(cam_img,(x,y),(x+w,y+h),(0,0,255),7)
            cv2.putText(cam_img,what_hazmat,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(200,0,0))
        cv2.imshow("Result",cam_img)
        '''kakitashi owari'''

        print(capture.get(cv2.CAP_PROP_FPS))

        key = cv2.waitKey(1)
        if key == 27: #ESCkey
            break
    except:
        print("error")
capture.release()
cv2.destroyAllWindows()
