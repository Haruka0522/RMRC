import glob
import shutil

directry =  glob.glob("./*")
a = input("enter except directry")
directry.remove(a)
save_dir = input("enter save directry")
num = int(input("serial num"))
for i in directry:
    files = glob.glob(i + "/*.jpg")
    for j in files:
        shutil.copy(j,save_dir+"neg"+str(num)+".jpg")
        num += 1
