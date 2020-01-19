import numpy as np
import cv2
import os

placards_path = "./hazmat-placards/"
camera_img = cv2.imread("IMG_20190615_070527.jpg")
result = []

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


#特徴抽出機の生成
detector = cv2.xfeatures2d.SIFT_create()

#グレースケールにする
camera_gray = cv2.cvtColor(camera_img,cv2.COLOR_BGR2GRAY)

#ブラーと２値化
camera_blur = cv2.GaussianBlur(camera_gray,(19,19),0)
img2 = cv2.threshold(camera_blur,140,240,cv2.THRESH_BINARY_INV)[1]

#輪郭検出
cnts = cv2.findContours(img2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]
'''
for pt in cnts:
    x,y,w,h = cv2.boundingRect(pt)
    if w < 100 or h < 100:
        continue
    cv2.rectangle(camera_img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imwrite("a.png",camera_img)
print(len(cnts))
'''
for pt in cnts:
    x,y,w,h = cv2.boundingRect(pt)
    if w > 100 and h > 100 and w < 800 and h < 378:   #輪郭の縦横が小さすぎたり大きすぎたりするものを弾く
        clipped = camera_gray[y:(y+h),x:(x+w)]
        #kp2,des2はカメラからの画像の特徴的な点の位置、特徴を表すベクトル
        kp2,des2 = detector.detectAndCompute(clipped,None)
        
        #このfor文で全てのハザードラベルを検討する
        ans = []
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
        
        result.append((x,y,w,h,hazmat_list[ans.index(max(ans))][1]))
print(ans)


#識別結果を画像に描画する
for x,y,w,h,sign in result:
    cv2.rectangle(camera_img,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.putText(camera_img,sign,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,0,0))
cv2.imwrite("result.jpg",camera_img)
