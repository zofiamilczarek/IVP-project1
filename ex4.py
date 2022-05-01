import numpy as np
from matplotlib import pyplot as plt
import cv2

def shiftImage(image,a,b):
    rows,columns= image.shape
    matrix = np.float32([[1,0,a],[0,1,b]])
    shiftedImage = cv2.warpAffine(image,matrix,(columns,rows))
    return shiftedImage


def ft(img):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    return 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))


image = cv2.imread('crayons.jpg',0)
image = cv2.resize(image,(1280,800))

shiftedImage = shiftImage(image,350,200)

#cv2.imshow('shift',shiftedImage)
#cv2.waitKey(0)

magnitudeShiftedImage = ft(shiftedImage)
magnitudeImage = ft(image)


plt.subplot(221),plt.imshow(image,cmap='gray')
plt.title('original image'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(shiftedImage,cmap='gray')
plt.title('shifted image'),plt.xticks([]),plt.yticks([])
plt.subplot(223), plt.imshow(magnitudeImage, cmap='gray')
plt.title('Magnitude of the original image'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(magnitudeShiftedImage, cmap='gray')
plt.title('Magnitude of the shifted image'), plt.xticks([]), plt.yticks([])
plt.show()