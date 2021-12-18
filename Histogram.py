import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("images/img2.jpg", 0)

cv.imshow("Original", img)

plt.subplot(131) 
plt.hist(img.ravel(), 256, [0, 256]) #flattened array(1D array)
plt.title('Original')



# Stretching Histogram
image2 = img
minv = np.amin(img)
maxv = np.amax(img)
h, w = img.shape[:2] #get the size of an image

for i in range(0, h-1, 1):
    for j in range(0, w-1, 1):
        image2[i, j] = ((img[i,j]-minv) / (maxv-minv)) * 255


cv.imshow('Stretched Image', image2)
plt.subplot(132) 
hist2 = cv.calcHist([image2], [0], None,[256], [0, 256])
plt.plot(hist2)
plt.title('Contrast Stretching')




# Equlization Histogram
image3 = cv.equalizeHist(cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY))
cv.imshow('Equalized Image', image3)

hist3 = cv.calcHist([image3], [0], None,[256], [0, 256])
plt.subplot(133) 
plt.plot(hist3)
plt.title('Histogram Equalization')



plt.show()
cv.waitKey()
cv.destroyAllWindows()