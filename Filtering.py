
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread("images/cat.jpg")
cv.imshow("Orginal Image", image)

#Gaussian filtering
smooth_image_gb = cv.GaussianBlur(image, (9, 9), 0) #blurs the image using a Gaussian kernel of size (9, 9)
cv.imshow("Gaussian Blur", smooth_image_gb)


#Averaging filter
smooth_image_b = cv.blur(image, (10, 10))
cv.imshow("Blur", smooth_image_b)

smooth_image_bfi = cv.boxFilter(image, -1, (10, 10), normalize=True)
cv.imshow("Box Filter", smooth_image_bfi)


# Median filtering
# blurs the image with a median kernel
smooth_image_mb = cv.medianBlur(image, 9)
cv.imshow("median Blur", smooth_image_mb)


# Bilateral filtering
# reduce noise while keeping the edges sharp
smooth_image_bf = cv.bilateralFilter(image, 5, 10, 10)
cv.imshow("bilateral Filter", smooth_image_bf)


# Sharpening images
smoothed = cv.GaussianBlur(image, (9, 9), 10)
cv.imshow("Smoothed", smoothed)

unsharped = cv.addWeighted(image, 1.5, smoothed, -0.5, 0)
cv.imshow("Sharp", unsharped)


cv.waitKey(0)
cv.destroyAllWindows()