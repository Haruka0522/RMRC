import numpy as np
import cv2
import csv

placards_path = "./hazmat-placards/"
GST_STR = 'nvarguscamerasrc \
    ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)30/1 \
    ! nvvidconv ! video/x-raw, width=(int)800, height=(int)600, format=(string)BGRx \
    ! videoconvert \
    ! appsink'

#hazmat_list = [(img1,name1),(img2,name2),・・・,(img26,name26)]
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

def get_feature_csv(img1,num):
    # 特徴量検出器の生成
    feature_detector = cv2.AKAZE_create()
    # 特徴量の検出と特徴量ベクトルの計算
    kp1, des1 = feature_detector.detectAndCompute(base_img, None)

    # ===== 特徴点と特徴量を同じ配列に生成しなおす
    numFeatures = len(kp1)
    kp_des_arry = []
    for i in range(numFeatures):
        # 特徴点の座標を格納
        kp_des = []
        kp_des.append(kp1[i].pt[0])  # x座標
        kp_des.append(kp1[i].pt[1])  # y座標
        # 特徴量ベクトルを格納
        numDescriptors = len(des1[i])
        for j in range(numDescriptors):
            kp_des.append(des1[i][j])
        # 特徴点の座用、特徴量ベクトルを一つの配列に格納
        kp_des_arry.append(kp_des)

     # ====== 特徴量ベクトルをcsvファイルに出力 =====
    csv_f = open('./'+str(num)+'-feature.csv', 'a')
    header = ['x', 'y', 'descriptor']
    writer = csv.writer(csv_f, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(kp_des_arry)

    # csvファイルを閉じる
    csv_f.close()
     
def classification(camera_img):

    # 特徴量検出器の生成
    feature_detector = cv2.AKAZE_create()
    
    good_qty = []
    for i in range(1,27):
         # 特徴量ベクトルが格納されたcsvファイルから特徴量を格納
         csv_file = str(i)+'-feature.csv'
         des1 = np.loadtxt(fname=csv_file,dtype=np.uint8,delimiter=",",skiprows=1,usecols=tuple(i for i in range(2,63)))
 
         # 特徴量の検出と特徴量ベクトルの計算
         kp2, des2 = feature_detector.detectAndCompute(camera_img, None)
 
         # Brute-Force Matcher生成
         bf = cv2.BFMatcher()
 
         # マッチング
         matches = bf.knnMatch(des1, des2, k=2)
 
         #良いデータのみ選別
         ratio = 0.5
         good_feature = []
         for m, n in matches:
             if m.distance < ratio * n.distance:
                 good_feature.append([m])
         good_qty.append(len(good_feature))
 
         #print(good_feature)
    print(good_qty.index(max(good_qty)))
    cv2.imwrite("RESULT.jpg",camera_img)


#===============================
#Main
#===============================
"""
for i in range(1,27):
    base_img = cv2.imread("./hazmat-placards/"+str(i)+".png")
    get_feature_csv(base_img,i)
"""
print("start")
img = cv2.imread("./IMG_20190615_070527.jpg")
classification(img)
