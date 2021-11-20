import cv2

# Read the image using imread function
orginalImage = cv2.imread("images/test4.jpg", cv2.IMREAD_COLOR)

# 1-Nearest
nearest = cv2.resize(orginalImage, (800,800),interpolation = cv2.INTER_NEAREST)

# 2-Linear
linear = cv2.resize(orginalImage, (800,800),interpolation = cv2.INTER_LINEAR)

#3-Cubic 
cubic = cv2.resize(orginalImage, (800,800), interpolation = cv2.INTER_CUBIC)

cv2.imshow("Orginal Image", orginalImage)
cv2.imshow("Nearest", nearest)
cv2.imshow("Linear", linear)
cv2.imshow("Cubic", cubic)

cv2.waitKey(0)
cv2.destroyAllWindows()
