import glob
f_list = glob.glob("./*.jpg")
with open("./poslist.txt",mode="w") as ng:
    for i in f_list:
        ng.write(i[2:]+'\n')
