from PIL import Image
import numpy as np

def pix_array(image):
    imarr=np.array(image)
    print(imarr)
    return imarr

def pixbo(im,data , l , b):
    imsi=im.size        #returns a tuple of size of image size tuple of (width x height x channels) channel - rgb=3 and rgba = 4
    
    if(imsi[0]>=l and imsi[1]>=b):
        boxlen=round(imsi[0]/l)
        boxbre=round(imsi[1]/b)

        for y in range(int(boxbre),int(imsi[1]),int(boxbre)):
            avg_r=0
            avg_g=0
            avg_b=0

            for x in range(int(boxlen),int(imsi[0]),int(boxlen)):
                for j in range(int(y-boxbre),int(y)):
                    for i in range(int(x-boxlen),int(x)):
                        avg_r+=data[j][i][0]
                        avg_g+=data[j][i][1]
                        avg_b+=data[j][i][2]

                avg_r/=(boxlen*boxbre)
                avg_g/=(boxlen*boxbre)
                avg_b/=(boxlen*boxbre)
                add_color(avg_r,avg_g,avg_b,boxlen,boxbre,data,x,y)
    return data


def add_color(avgr,avgg,avgb,boxlen,boxbre,data,x,y):
    for j in range(int(y-boxbre),int(y)):
        for i in range(int(x-boxlen),int(x)):
            data[j][i][0]=avgr
            data[j][i][1]=avgg
            data[j][i][2]=avgb
