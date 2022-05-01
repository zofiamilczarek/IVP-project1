import copy
import math

import numpy as np
from matplotlib import pyplot as plt
import cv2

def cartesianToPolar(img):
    rows,columns,_ = img.shape
    center = (int(rows / 2), int(columns / 2))
    maxRadius = math.sqrt((rows/2.0)**2.0 + (columns/2.0)**2.0)
    polar = cv2.linearPolar(img,center,maxRadius,cv2.WARP_FILL_OUTLIERS)
    return polar


def contour(img,thresh):
    imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _, imThresh = cv2.threshold(imGray, thresh, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(imThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contourIMG = np.ones(img.shape)
    return cv2.drawContours(contourIMG,contours,-1,(0,0,0),thickness = cv2.FILLED)



im1 = cv2.imread('crayons.jpg')
im2 = cv2.imread('perspective.jpg')
#im1 = im2

polar1 = copy.deepcopy(im1)
polar2 = copy.deepcopy(im2)

polar1 = cartesianToPolar(polar1)
polar2 = cartesianToPolar(polar2)

cv2.imshow('normal 1',im1)
cv2.imshow('polar 1',polar1)
cv2.waitKey(0)

cv2.imshow('normal 2',im2)
cv2.imshow('polar 2',polar2)
cv2.waitKey(0)

im1contour = contour(im1,100)
im2contour = contour(im2,100)

cv2.imshow("contours im1",im1contour)
cv2.waitKey(0)

cv2.imshow("contours im2",im2contour)
cv2.waitKey(0)