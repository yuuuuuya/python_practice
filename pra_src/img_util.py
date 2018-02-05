import numpy as np
import matplotlib.pyplot as plt
import pdb
import os
'''
The first line import "Numetric(suuti) calsurlation module"
The second line enable to indicate(hyoujisuru) a image and achart.
The third line enable to talk with a python.
The fourth line import os module. Refarence URL:"http://nonbiri-tereka.hatenablog.com/entry/2014/03/14/195241"
'''

figsaveTo = '../figures/'
'''
どこで使っているか。
'''

def color_adjust(image):
    return image[:, :, [2,1,0]]
'''
This adjust(tyousei) the RGB color order of the image array.
'''

def rotateLeft_bi90(image):
    aligned_img= image.transpose([1,0,2])
    new_Xindices = aligned_img.shape[0] - np.array(range(aligned_img.shape[0])) -1
    img2=aligned_img[new_Xindices]
    return img2
'''
This adjust is "relotate of the image"
'''

def extract_image(img, faceLoc, color = True):

    cornerX, cornerY, lenX, lenY = faceLoc
    xRange = range(cornerX, cornerX + lenX)
    yRange = range(cornerY, cornerY + lenY)
    return img[cornerX:(cornerX+lenX), cornerY:(cornerY+lenY), :]
'''
The order extract(nukidasu) picture range of cornerX+lenX to cornerY+lenY.
RefarenceURL:http://qiita.com/supersaiakujin/items/d63c73bb7b5aac43898a
'''

def fix_face_location(rects):
    rectsNew = rects.copy()
    for k in range(len(rects)):
        rectsNew[k][1] = rects[k][0]
        rectsNew[k][0] = rects[k][1]
    return rectsNew
'''
copy() is contents of for
'''

def draw_rectangle(img, faceLoc, color = [255, 255, 255], thickness = 5):
    locX= faceLoc[0]
    locY= faceLoc[1]
    lenX= faceLoc[2]
    lenY= faceLoc[3]
    newimg = img.copy()
    newimg[locX:locX+thickness, locY: locY+lenY] = color
    newimg[locX: locX+lenX,  locY:locY+thickness] = color
    newimg[locX +lenX:locX +lenX+thickness, locY: locY+lenY] = color
    newimg[locX: locX+lenX,  locY+lenY:locY+lenY+thickness] = color

    #newimg[locX:locX+lenX+thickness, locY: locY+lenY] = color
    return newimg


def draw_multiple_rectangles(img, faceRects, color = [255, 255, 255], thickness = 5, save = False, filename = 'test.jpg'):
    imgnow = img

    for k in range(len(faceRects)):

        faceLoc = faceRects[k]
        #pdb.set_trace()

        imgnow =  draw_rectangle(imgnow, faceLoc, color = color, thickness = thickness)

    if save:
        plt.figure(figsize = (20,20) )
        plt.imshow(imgnow)
        figpath = os.path.join(figsaveTo, filename)
        plt.savefig(figpath)

    return imgnow
