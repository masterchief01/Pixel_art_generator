import matplotlib.pyplot as plot
from PIL import Image
import numpy as np
import scipy.misc as misc
from pixel_ops import *
import sys, os

def pix_array(image):
    imarr=np.array(image)
    return imarr

# def pixbo(im,data , l , b):
#     imsi=im.size
    
#     if(500>=l and 500>=b):
#         boxlen=round(imsi[0]/l)
#         boxbre=round(imsi[1]/b)

#         for y in range(int(boxbre),int(imsi[1]),int(boxbre)):
#             avg_r=0
#             avg_g=0
#             avg_b=0

#             for x in range(int(boxlen),int(imsi[0]),int(boxlen)):
#                 for j in range(int(y-boxbre),int(y)):
#                     for i in range(int(x-boxlen),int(x)):
#                         avg_r+=data[j][i][0]
#                         avg_g+=data[j][i][1]
#                         avg_b+=data[j][i][2]

#                 avg_r/=(boxlen*boxbre)
#                 avg_g/=(boxlen*boxbre)
#                 avg_b/=(boxlen*boxbre)
#                 add_color(avg_r,avg_g,avg_b,boxlen,boxbre,data,x,y)
#     return data


# def add_color(avgr,avgg,avgb,boxlen,boxbre,data,x,y):
#     for j in range(int(y-boxbre),int(y)):
#         for i in range(int(x-boxlen),int(x)):
#             data[j][i][0]=avgr
#             data[j][i][1]=avgg
#             data[j][i][2]=avgb



if __name__=="__main__":
    script_dir = sys.path[0]
    img_path = os.path.join(script_dir , "")	#IMPORTANT! insert image path here!
    image = Image.open(img_path)
#   image=Image.open("1515472517.png")
    image_array=pix_array(image)

    count = 0 
    while(count!=1):
        
        l=int(input("Length of the image: "))
        b=int(input("Breadth of the image: "))

        if(l<=500 and b<=500):
            # print(image_array)        test difference between the initial and new array
            imarr=pixbo(image,image_array,l,b)
            # print('stop')
            # print(imarr)
            plot.imshow(image_array)
            plot.show()
            count = 1
        else:
            print('Image cannot be pixilated') 
        
