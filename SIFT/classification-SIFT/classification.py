import numpy as np
import cv2
import os

placards_path = "./hazmat-placards/"
hazmat_placards = [placards_path + sign_name for sign_name in os.listdir(placards_path)]
img2 = cv2.imread("IMG_20190615_070527.jpg",0)
ans = []


#hazmat_list = [(img1,name1),(img2,name2),・・・,(img26,name26)]
hazmat_list = list()
hazmat_list.append((cv2.imread(placards_path+"1.png",0),"1.1 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"2.png",0),"1.2 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"3.png",0),"1.3 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"4.png",0),"1.4 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"5.png",0),"1.5 Blasting Agent"))
hazmat_list.append((cv2.imread(placards_path+"6.png",0),"1.6 Explosives"))
hazmat_list.append((cv2.imread(placards_path+"7.png",0),"Flammable Gas"))
hazmat_list.append((cv2.imread(placards_path+"8.png",0),"Inhalation Hazard 2"))
hazmat_list.append((cv2.imread(placards_path+"9.png",0),"Non Flammable Gas"))
hazmat_list.append((cv2.imread(placards_path+"10.png",0),"Oxygen"))
hazmat_list.append((cv2.imread(placards_path+"11.png",0),"Combustible"))
hazmat_list.append((cv2.imread(placards_path+"12.png",0),"Flammable"))
hazmat_list.append((cv2.imread(placards_path+"13.png",0),"Fuel Oil"))
hazmat_list.append((cv2.imread(placards_path+"14.png",0),"Gasoline"))
hazmat_list.append((cv2.imread(placards_path+"15.png",0),"Dangerous When Wet"))
hazmat_list.append((cv2.imread(placards_path+"16.png",0),"Flammable Solid"))
hazmat_list.append((cv2.imread(placards_path+"17.png",0),"Spontaneously Combustible"))
hazmat_list.append((cv2.imread(placards_path+"18.png",0),"Oxidizer"))
hazmat_list.append((cv2.imread(placards_path+"19.png",0),"Organic Peroxide"))
hazmat_list.append((cv2.imread(placards_path+"20.png",0),"Inhalation Hazard 6"))
hazmat_list.append((cv2.imread(placards_path+"21.png",0),"Poison"))
hazmat_list.append((cv2.imread(placards_path+"22.png",0),"Toxic"))
hazmat_list.append((cv2.imread(placards_path+"23.png",0),"Radioactive"))
hazmat_list.append((cv2.imread(placards_path+"24.png",0),"Corrosive"))
hazmat_list.append((cv2.imread(placards_path+"25.png",0),"Other Dangerous Goods"))
hazmat_list.append((cv2.imread(placards_path+"26.png",0),"Dangerous"))


#特徴抽出機の生成
detector = cv2.xfeatures2d.SIFT_create()

#kp2,des2はカメラからの画像の特徴的な点の位置、特徴を表すベクトル
kp2,des2 = detector.detectAndCompute(img2,None)

#このfor文で全てのハザードラベルを検討する
for placard in hazmat_list:
    #kp1,des1はハザードラベルの特徴的な点の位置、特徴を表すベクトル
    kp1,des1 = detector.detectAndCompute(placard[0],None)

    #特徴点の比較
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    
    #割合試験を適用
    good = []
    match_param = 0.6
    for m,n in matches:
        if m.distance < match_param * n.distance:
            good.append([m])

    #適合している点の個数をリストansに突っ込む
    ans.append(len(good))

print(hazmat_list[ans.index(max(ans))][1])
