
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/hat.jpg", cv2.IMREAD_COLOR)
res = cv2.resize(img, None, fx=10, fy=10, interpolation = cv2.INTER_LINEAR)

#OR

# height, width = img.shape[:2]
# res = cv2.resize(img,(20 * width, 20 * height), interpolation = cv2.INTER_CUBIC)

plt.subplot(121), plt.imshow(img), plt.title('Input') # mnp = 121 rows/columns/num
plt.subplot(122), plt.imshow(res), plt.title('Output')
plt.show()