# -*- coding: utf-8 -*-
import cv2
import csv
import numpy as np
 
def get_feature(img1):
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
    csv_f = open('./feature.csv', 'w')
    header = ['x', 'y', 'descriptor']
    writer = csv.writer(csv_f, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(kp_des_arry)
 
    # csvファイルを閉じる
    csv_f.close()
 
def vetor_matching(img):
    # 特徴量検出器の生成
    feature_detector = cv2.AKAZE_create()
 
    # 特徴量ベクトルが格納されたcsvファイルから特徴量を格納
    kp1 = np.loadtxt(fname='feature.csv',dtype="uint8",delimiter=",",skiprows=1,usecols=(0,1))
    des1 = np.loadtxt(fname='feature.csv', dtype="uint8", delimiter=",", skiprows=1, usecols = (range(2, 63)))
 
    # 特徴量の検出と特徴量ベクトルの計算
    kp2, des2 = feature_detector.detectAndCompute(img, None)
 
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
    img3 = cv2.drawMatchesKnn(base_img,kp1,img,kp2,good_feature,None,flags=2)
    cv2.imshow(img3)
    print(good_feature)
 
 
if __name__ == '__main__':
    # 画像の読み込み
    base_img = cv2.imread("./hazmat-placards/1.png")
    img = cv2.imread("IMG_20190615_070527.jpg")
 
    # base_imgの特徴量をcsvファイルに出力
    get_feature(base_img)
 
    # ベース画像の特徴量を配列として格納し、特徴量ベクトルの配列でマッチング
    vetor_matching(img)
