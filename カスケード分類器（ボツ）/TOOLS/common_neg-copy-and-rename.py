import glob
import shutil

directory =  glob.glob("./*")

save_dir = input("enter save directory")
num = int(input("serial num"))

for i in directory:
    shutil.copy(i,save_dir+"neg"+str(num)+".jpg")
    num += 1
