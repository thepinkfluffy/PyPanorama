from PIL import Image
import os
import pathlib
import warnings
import ctypes
warnings.filterwarnings("ignore")
try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
if not is_admin:
    print("admin access required")
    exit()
if not os.path.exists(r""+str(pathlib.Path().absolute())+"\panorama.jpg"):
    print("panorama.jpg doesn't exist in this directory")
    exit()
im = Image.open(r""+str(pathlib.Path().absolute())+"\panorama.jpg")
width, height = im.size
aspect = int(input("What aspect ratio do you want for the output pictures?:\n1)1:1\n2)1.91:1(landscape)\n3)4:5(portrait)\n"))
if aspect != 3 and aspect != 2 and aspect != 1:
    print("please specify a correct aspect")
    exit()
print("how many pics do you want? ( The Instagram upload limit is 10)")
if aspect == 1:
    print("the max amount for these settings is "+str(int( width/height)))
if aspect == 2:
    print("the max amount for these settings is "+str(int( width/(height*1.91))))
if aspect == 3:
    print("the max amount for these settings is "+str(int( width/(height*0.8))))
pics = int(input(""))
if aspect == 1:
    if height*pics > width:
        print("the width of the source image doesn't allow for this number of pictures")
        exit()
elif aspect == 2:
    if (height*1.91)*pics > width:
        print("the width of the source image doesn't allow for this number of pictures")
        exit()
elif aspect == 3:
    if (height*0.8)*pics > width:
        print("the width of the source image doesn't allow for this number of pictures")
        exit()
folderpath = r""+str(pathlib.Path().absolute())+"\output_files"
counter = 0
if not os.path.exists(folderpath):
    os.makedirs(folderpath)
else:
    while True:
        counter+=1
        folderpath = r""+str(pathlib.Path().absolute())+"\output_files"+str(counter)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
            break

for x in range(1,pics+1):
    if aspect == 1:
        square = ((x-1)*height,0,height*x,height)
    elif aspect == 2:
        square = ((x-1)*height*1.91,0,height*x*1.91,height)
    elif aspect == 3:
        square = ((x-1)*height*0.8,0,height*x*0.8,height)
    c_i = im.crop(box=square)
    c_i.save(str(folderpath)+"\output"+str(x)+".jpg")
print("done")
print("output files are in "+str(folderpath))