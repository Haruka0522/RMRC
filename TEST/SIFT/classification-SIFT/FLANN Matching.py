import numpy as np
import cv2
from time import sleep
import os

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
def classificate(img):
    #特徴抽出機の生成
    #detector = cv2.xfeatures2d.SIFT_create()

    #グレースケールにする
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #ブラーと２値化
    img = cv2.GaussianBlur(img,(9,9),1)
    img = cv2.threshold(img,0,255,cv2.THRESH_OTSU)[1]

    kp_img,des_img = detector.detectAndCompute(img,None)

    #このfor文で全てのハザードラベルを検討する
    ans = []
    for kp,des in kp_des_list:
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
        search_params = dict(checks=50)

        flann = cv2.FlannBasedMatcher(index_params,search_params)

        matches = flann.knnMatch(des,des_img,k=2)

        matchesMask = [[0,0] for i in range(len(matches))]

        good = 0
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.9*n.distance:
                good += 1


        #適合している点の個数をリストansに突っ込む
        ans.append(good)

    print(ans)
    #print(hazmat_list[ans.index(max(ans))][1])


#------------------------------------------------------
#
#main loop
#
#------------------------------------------------------
while True:
    #try:
    cam_ret,cam_img = capture.read()
    if cam_ret != True:
        print("No ret")
        continue
    cam_gray_img = cv2.cvtColor(cam_img,cv2.COLOR_BGR2GRAY)
    classificate(cam_gray_img)
    #cv2.imshow("cam",cam_gray_img)
    """
    cam_img = cv2.GaussianBlur(cam_gray_img,(11,11),0)
    im2 = cv2.threshold(cam_img,140,240,cv2.THRESH_BINARY_INV)[1]
    cnts = cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
    for pt in cnts:
        x,y,w,h = cv2.boundingRect(pt)
        if w > 100 and h > 100 and w < 500 and h < 500:   #輪郭の縦横が小さすぎたり大きすぎたりするものを弾く
            clipped = cam_gray_img[y:(y+h),x:(x+w)]
            cv2.imshow("clipped",clipped)
            classificate(clipped)
    """
    key = cv2.waitKey(10)
    if key == 27: #ESC
        break
    #except:
        #print("error")

capture.release()
cv2.destroyAllWindows()
