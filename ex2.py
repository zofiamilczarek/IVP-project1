import copy

import numpy as np
from matplotlib import pyplot as plt
import cv2

def applyPointWise(value):
    value = 255 - value
    return value

def applyPowerPointWise(value,n):
    s = pow(value,n)
    return s

def applyPointWiseToImage(image):
    rows, cols = image.shape
    newImage = copy.copy(image)
    print(newImage[0][0])
    for r in range(rows):
        for c in range(cols):
            newImage[r][c] = applyPointWise(image[r][c])
    return newImage

def applyPowerPointWiseToImage(image):
    rows, cols = image.shape
    newImage = copy.copy(image)
    print(newImage[0][0])
    for r in range(rows):
        for c in range(cols):
            newImage[r][c] = applyPowerPointWise(image[r][c],0.6)
    return newImage

lowContrast = cv2.imread('fog.jpg',0)
plt.hist(lowContrast.ravel(),256,[0,256])
lowContrast = cv2.resize(lowContrast,(1280,800))
plt.title("Low contrast histogram")
#plt.show()

vals = [3,3,3]
print(lowContrast.shape)

#histLowContrast = cv.calcHist([lowContrast],[0],None,[256],[0,256])

highContrast = cv2.imread('shadows.jpg',0)
plt.subplot(121),plt.hist(highContrast.ravel(),256,[0,256])
plt.title("High contrast histogram")
#plt.show()

#histHighContrast = cv.calcHist([highContrast],[0],None,[256],[0,256])
negativeLowContrast = copy.deepcopy(lowContrast)
negativeLowContrast = applyPointWiseToImage(negativeLowContrast)
#cv2.imshow('Low contrast negative',negativeLowContrast)

negativeHighContrast = copy.deepcopy(highContrast)
negativeHighContrast = applyPointWiseToImage(negativeHighContrast)
#cv2.imshow('High contrast negative',negativeHighContrast)

plt.hist(negativeLowContrast.ravel(),256,[0,256])
#plt.show()
plt.hist(negativeHighContrast.ravel(),256,[0,256])
#plt.show()

highContrastPower = copy.deepcopy(highContrast)
highContrastPower = applyPowerPointWiseToImage(highContrastPower)

cv2.imshow('high contrast corrected',highContrastPower)

cv2.waitKey(0)
