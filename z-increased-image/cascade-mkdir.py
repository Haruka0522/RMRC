import os
import glob

directories = glob.glob("./*")
for i in directories:
    try:
        os.mkdir("."+i)
        os.mkdir("."+i+"/neg")
        os.mkdir("."+i+"/pos")
        os.mkdir("."+i+"/cascade")
        os.mkdir("."+i+"/vec")
    except:
        print(i+" exist")
