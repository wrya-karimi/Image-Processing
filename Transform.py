import numpy as np
import cv2
import matplotlib.pylab as plt

# Read the image using imread function
img = cv2.imread("images/child.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')

plt.subplot(231) 
plt.imshow(img)
plt.title('Original')

rows, cols, dim = img.shape

# Transform image
M = np.float32([[1, 0, 40], # M: transformation matrix
                [0, 1, 40],
                [0, 0, 1]])

transformImage = cv2.warpPerspective(img, M, (cols, rows))
plt.subplot(232) 
plt.imshow(transformImage)
plt.title('Transform')

# Scaling
M = np.float32([[1.2, 0, 0], # M: transformation matrix
                [0, 1.2, 0],
                [0, 0, 1]])

scaleImage = cv2.warpPerspective(img, M, (cols, rows))
plt.subplot(233) 
plt.imshow(scaleImage)
plt.title('Scaling')

# X-Axis Shearing
M = np.float32([[1, 0.6, 0], # M: transformation matrix
                [0, 1, 0],
                [0, 0, 1]])

shearing = cv2.warpPerspective(img, M, (cols, rows))
plt.subplot(234) 
plt.imshow(shearing)
plt.title('X-Axis Shearing')

# X-Axis Reflection
M = np.float32([[1, 0, 0], # M: transformation matrix
                [0, -1 , rows],
                [0, 0, 1]])

reflection = cv2.warpPerspective(img, M, (cols, rows))
plt.subplot(235) 
plt.imshow(reflection)
plt.title('X-Axis Reflection')

# Y-Axis Reflection
M = np.float32([[-1, 0, cols], # M: transformation matrix
                [0, 1 , 0],
                [0, 0, 1]])

reflectionY = cv2.warpPerspective(img, M, (cols, rows))
plt.subplot(236) 
plt.imshow(reflectionY)
plt.title('Y-Axis Reflection')

plt.show()