import os
import cv2
import numpy as np

path = "/home/haruka/RMRC/resized-HazmatPlacards/"
save_path = "/home/haruka/RMRC/increased-picture/"
rotation_angle = [0,45,90,135,180,225,270,315]
original_img_list = os.listdir(path)

def Rotation(src,angle):
    height = src.shape[0]
    width = src.shape[1]
    center = (int(width/2),int(height/2))
    scale = 1.0
    trans = cv2.getRotationMatrix2D(center,angle,scale)
    image2 = cv2.warpAffine(src,trans,(width,height))
    return image2

def HighContrast(src):
    # ルックアップテーブルの生成
    min_table = 50
    max_table = 205
    diff_table = max_table - min_table
    
    LUT_HC = np.arange(256, dtype = 'uint8' )
    
    # ハイコントラストLUT作成
    for i in range(0, min_table):
        LUT_HC[i] = 0
    for i in range(min_table, max_table):
        LUT_HC[i] = 255 * (i - min_table) / diff_table
    for i in range(max_table, 255):
        LUT_HC[i] = 255

    high_cont_img = cv2.LUT(src,LUT_HC)
    return high_cont_img

def LowContrast(src):
    # ルックアップテーブルの生成
    min_table = 50
    max_table = 205
    diff_table = max_table - min_table
    
    LUT_LC = np.arange(256, dtype = 'uint8' )
    
    # ローコントラストLUT作成
    for i in range(256):
        LUT_LC[i] = min_table + i * (diff_table) / 255
    
    low_cont_img = cv2.LUT(src,LUT_LC)
    return low_cont_img

def Smoosing(src):
    average_square = (10,10)
    blur_img = cv2.blur(src,average_square)
    return blur_img

def GaussianNoise(src):
    row,col,ch = src.shape
    mean = 0
    sigma = 15
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    gauss_img = src + gauss
    return gauss_img

def SaltNoise(src):
    row,col,ch = src.shape
    s_vs_p = 0.5
    amount = 0.004
    salt_img = src.copy()

    num_salt = np.ceil(amount * src.size * s_vs_p)
    coords = [np.random.randint(0, i-1 , int(num_salt)) for i in src.shape]
    salt_img[coords[:-1]] = (255,255,255)
    return salt_img

def PepperNoise(src):
    row,col,ch = src.shape
    s_vs_p = 0.5
    amount = 0.004
    pepper_img = src.copy()

    num_pepper = np.ceil(amount* src.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1 , int(num_pepper)) for i in src.shape]
    pepper_img[coords[:-1]] = (0,0,0)
    return pepper_img


if __name__ == '__main__':
    #保存先がないときにディレクトリを作る
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    num = 0
    for original_img in original_img_list:
        img = cv2.imread(path+"/"+original_img,1)
        converted_img = []
        for angle in rotation_angle:
            rotated_img = Rotation(img,angle)
            converted_img.append(rotated_img)
            converted_img.append(HighContrast(rotated_img))
            converted_img.append(LowContrast(rotated_img))
            converted_img.append(Smoosing(rotated_img))
            converted_img.append(GaussianNoise(rotated_img))
            converted_img.append(SaltNoise(rotated_img))
            converted_img.append(PepperNoise(rotated_img))

    for num,img in enumerate(converted_img):
        cv2.imwrite(save_path + str(num) + ".jpg",img)
