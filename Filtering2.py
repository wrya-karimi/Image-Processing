import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import rescale
from scipy.signal import convolve2d
import cv2 as cv


image = imread("images/child.jpg")
plt.imshow(image, cmap='gray')

image2 = rescale(rgb2gray(image), 1)

# Edge Detection1
kernel1 = np.array([[0, -1, 0],
                    [-1, 4, -1],
                    [0, -1, 0]])


# Edge Detection2
kernel2 = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])


# Bottom Sobel Filter
kernel3 = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])



kernels = [kernel1, kernel2, kernel3]
kernel_name = ['Edge Detection#1', 'Edge Detection#2', 'Bottom Sobel']
figure, axis = plt.subplots(1,3, figsize=(12,10))

for kernel, name, ax in zip(kernels, kernel_name, axis.flatten()):
     conv_im1 = convolve2d(image2, kernel[::-1, ::-1]).clip(0,1)
     ax.imshow(abs(conv_im1), cmap='gray')
     ax.set_title(name)

cv.waitKey(0)
cv.destroyAllWindows()