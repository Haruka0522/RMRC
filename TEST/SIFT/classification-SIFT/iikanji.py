import cv2
import numpy as np

#------------------------------------------------------------
#
#Constant Definition
#
#------------------------------------------------------------
RESIZE_RATIO = 0.3

MIN_MATCH_COUNT = 100

MIN_AREA = 35000

MATCHING_RATIO = 0.6

CLASSES_COUNT = 1

TEMPLATE_IMAGES_PATH = "/home/haruka/RMRC/hazmat_label2020/"


#------------------------------------------------------------
#
#Function definition
#
#------------------------------------------------------------
def display(cv_img):
    cv2.imshow("result",cv_img)
    cv2.waitKey(1)

def gamma_filter(cv_img):
    gamma_cvt = np.zeros((256,1),dtype='uint8')
    for i in range(256):
        gamma_cvt[i][0] = 255*(float(i)/255)**(1.0/1.8)
    result = cv2.LUT(cv_img,gamma_cvt)
    return result

def template_resizer(cv_img):
    h = cv_img[0]
    w = cv_img[1]
    result = cv2.resize(cv_img,(int(h*RESIZE_RATIO),int(w*RESIZE_RATIO)))
    return result

#------------------------------------------------------------
#
#Import Template Images
#
#------------------------------------------------------------
hazmat_list = []
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-1.3-explosive.png"),"1.3 Explosives"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-1.4-explosive.png"),"1.4 Explosives"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-1.5-blasting-agent.png"),"1.5 Blasting Agent"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-2-flammable-gas.png"),"Flammable Gas"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-2-poison-gas.png"),"Poison Gas"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-3-flammable-liquid.png"),"Flammable Liquid"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-4-dangerous-when-wet.png"),"Dangerous When Wet"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-4-spontaneously-combustible.png"),"Spontaneously Combustible"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-5.1-oxidizer.png"),"Oxidizer"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-6-infectious-substance.png"),"Infectious Substance"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-6-poison-inhalation-hazard.png"),"Inhalation Hazard"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-6-poison.png"),"Poison"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-7-radioactive-ii.png"),"Radioactive ii"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-7-radioactive-iii.png"),"Radioactive iii"))
hazmat_list.append((cv2.imread(TEMPLATE_IMAGES_PATH+"label-8-corrosive.png"),"Corrosive"))


#------------------------------------------------------------
#
#Preparation
#
#------------------------------------------------------------
sift = cv2.xfeatures2d.SIFT_create()

kp1 , des1 = sift.detectAndCompute(hazmat_list[0][0] ,None)
kp2 , des2 = sift.detectAndCompute(hazmat_list[1][0] ,None)
kp3 , des3 = sift.detectAndCompute(hazmat_list[2][0] ,None)
kp4 , des4 = sift.detectAndCompute(hazmat_list[3][0] ,None)
kp5 , des5 = sift.detectAndCompute(hazmat_list[4][0] ,None)
kp6 , des6 = sift.detectAndCompute(hazmat_list[5][0] ,None)
kp7 , des7 = sift.detectAndCompute(hazmat_list[6][0] ,None)
kp8 , des8 = sift.detectAndCompute(hazmat_list[7][0] ,None)
kp9 , des9 = sift.detectAndCompute(hazmat_list[8][0] ,None)
kp10,des10 = sift.detectAndCompute(hazmat_list[9][0] ,None)
kp11,des11 = sift.detectAndCompute(hazmat_list[10][0],None)
kp12,des12 = sift.detectAndCompute(hazmat_list[11][0],None)
kp13,des13 = sift.detectAndCompute(hazmat_list[12][0],None)
kp14,des14 = sift.detectAndCompute(hazmat_list[13][0],None)
kp15,des15 = sift.detectAndCompute(hazmat_list[14][0],None)

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



def main():
    capture = cv2.VideoCapture(2)
    sift = cv2.xfeatures2d.SIFT_create()
    while True:
        try:
            cam_ret,cam_img = capture.read()
            if cam_ret != True:
                print("No ret")
                continue
            result_img = cam_img.copy()
            kp_cam,des_cam = sift.detectAndCompute(cam_img,None)
            for i,(kp_temp,des_temp) in enumerate(kp_des_list):
                bf = cv2.BFMatcher()
                matches = bf.knnMatch(des_temp,des_cam,k=2)
                good = []
                for m,n in matches:
                    if m.distance < MATCHING_RATIO * n.distance:
                        good.append(m)
                #print(len(good))
                if len(good) > MIN_MATCH_COUNT:
                    src_pts = np.float32([kp_temp[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
                    dst_pts = np.float32([ kp_cam[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
                    M, mask = cv2.findHomography(src_pts,dst_pts,cv2.RANSAC,5.0)
                    matchesMask = mask.ravel().tolist()
                    h,w = 1188,1188 #h,w = temp_img.shape
                    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
                    dst = cv2.perspectiveTransform(pts,M)
                    #print(cv2.contourArea(np.int32(dst))) 面積デバッグ
                    if cv2.contourArea(np.int32(dst)) < MIN_AREA:
                        continue
                    result_img = cv2.polylines(cam_img,[np.int32(dst)],True,(0,255,0),8,cv2.LINE_AA)
                    result_img = cv2.putText(result_img,hazmat_list[i][1],tuple(dst[1,0]),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=3)
                else:
                    matchesMask = None
                #draw_params = dict(matchColor = (0,255,0), #matching line color (green)
                #                   singlePointColor = None,
                #                   matchesMask = matchesMask, #only inliers
                #                   flags = 2)
                #result_img = cv2.drawMatches(hazmat_list[i][0],kp_temp,cam_img,kp_cam,good,None,**draw_params)
            display(result_img)

        except KeyboardInterrupt:
            print("Ctrl-C Shutting down")
            break
        except:
            print("Error")
    capture.release()
    cv2.destoryAllWindows()


if __name__ == '__main__':
    main()

