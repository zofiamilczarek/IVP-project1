import copy

import cv2
import numpy as np
import matplotlib.pyplot as plt

def hue(blue, green, red):
    """ takes a pixel with floored b/g/r values"""
    chroma = max(blue,green,red)
    hue = 0
    if chroma == 0:
        hue=0
    elif chroma == red:
        hue = 60*(((green-blue)/chroma) % 6)
    elif chroma == green:
        60*((blue - red)/chroma + 2)
    elif chroma == blue:
        60*((red-green)/chroma + 4)
    return hue
#AAAAAAAAAAAAaaaaaa
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa
#c REMEMBER TO MAKE H AND S GREYSCALE AND THEN I/V IS THE ONLY THING U COMPUTE
def bgr2hsv(values):
    """ converts a pixel from bgr to hsv """
    red = values[0]/255
    green = values[1]/255
    blue = values[2]/255
    h= hue(blue,green,red)
    chroma = max(blue,green,red) - min(blue,green,red)
    value = max(blue,green,red)
    if value!=0:
        saturation = chroma/value
    else:
        saturation = 0
    values[0] = 255*h
    values[1] = 255*saturation
    values[2] = 255*value
    return values

def bgr2hsi(values):
    """ converts a pixel from bgr to hsi"""
    blue = values[0]/255 #values are floored
    green = values[1]/255
    red = values[2]/255
    h = hue(blue,green,red)
    intensity = (red+blue+green)/3
    if intensity!=0:
        saturation = min(blue,green,red)/intensity
    else:
        saturation = 0
    values[0] = 255*h #values are enlarged back to [0,255] range
    values[1] = 255*saturation
    values[2] = 255*intensity
    return values


def convertBGR(code,image):
    newImage = np.copy(image)
    rows,cols,_ = image.shape
    for r in range(rows):
        for c in range(cols):
            if code == "HSI":
                newImage[r][c] = bgr2hsi(image[r][c])
            elif code== "HSV":
                newImage[r][c] = bgr2hsv(image[r][c])
    return newImage

def showConvertion(code,name,image):
    hsiImage = copy.deepcopy(image)
    hsiImage = convertBGR(code,hsiImage)
    cv2.imshow(code+' image : my function, '+name,hsiImage)

def convertAll(name, image):
    showConvertion('HSI', name, image)
    showConvertion('HSV', name, image)
    colorfulHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('original image, '+name, image)
    cv2.imshow('HSV image: inbuilt function, '+name, colorfulHSV)

colorfulImageRGB = cv2.imread('birds.jpg')
colorfulImageRGB = cv2.resize(colorfulImageRGB,(1280,800))
bleakImageRGB = cv2.imread('stone.jpg')

colorfulHSV = copy.deepcopy(colorfulImageRGB)
colorfulHSV = convertBGR('HSV',colorfulHSV)
bleakHSV = copy.deepcopy(bleakImageRGB)
bleakHSV = convertBGR('HSV',bleakHSV)

colorfulHSI = copy.deepcopy(colorfulImageRGB)
colorfulHSI = convertBGR('HSI',colorfulHSI)
bleakHSI = copy.deepcopy(bleakImageRGB)
bleakHSI = convertBGR('HSI',bleakHSI)

plt.subplot(321),plt.imshow(colorfulImageRGB,cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(322),plt.imshow(bleakImageRGB,cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])

plt.subplot(323), plt.imshow(colorfulHSV, cmap='gray')
plt.title('colorful HSV'), plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(bleakHSV, cmap='gray')
plt.title('bleak HSV'), plt.xticks([]), plt.yticks([])

plt.subplot(325), plt.imshow(colorfulHSI, cmap='gray')
plt.title('colorful HSI'), plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(bleakHSI, cmap='gray')
plt.title('bleak HSI'), plt.xticks([]), plt.yticks([])
plt.show()