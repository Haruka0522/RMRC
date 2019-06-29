import glob
f_list = glob.glob("./neg/*.jpg")
with open("./nglist.txt",mode="w") as ng:
    for i in f_list:
        ng.write(i[2:]+'\n')
