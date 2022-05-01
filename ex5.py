import copy
import random

import numpy as np
from matplotlib import pyplot as plt
import cv2

#adding salt and pepper noise, assumes a greyscale
def addnoise(image):
    noisedImage = np.copy(image)
    rows,columns = image.shape
    numberOfWhitePixels = random.randint(int(image.size*0.3),int(image.size*0.9))
    numberOfBlackPixels = random.randint(int(image.size*0.3),int(image.size*0.9))
    for i in range(numberOfWhitePixels):
        x = random.randint(0,rows-1)
        y = random.randint(0,columns-1)
        noisedImage[x][y] = 255
    for i in range(numberOfBlackPixels):
        x = random.randint(0,rows-1)
        y = random.randint(0,columns-1)
        noisedImage[x][y]=0
    return noisedImage

def ft(img):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    return 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

#def removeNoise(image):


image =  cv2.imread('pink.jpg',0)
image

noisedImage = addnoise(image)

plt.subplot(231),plt.imshow(image,cmap='gray')
plt.title('original image'),plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(noisedImage,cmap='gray')
plt.title('image with s&p noise'),plt.xticks([]),plt.yticks([])
plt.show()