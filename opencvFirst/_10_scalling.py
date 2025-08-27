# Scaling Images
# In this code we will learn how to scale images using OpenCV. Scaling is the process of resizing an image either by a specific size or by a scaling factor.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('./img/binary1.png')

resized_image = cv2.resize(img1, (300, 300))
cv2.imshow('Resized Image', resized_image)

# Scaling by factor 
img_half = cv2.resize(resized_image, None, fx=0.5, fy=0.5)
img_double = cv2.resize(resized_image, None, fx=2, fy=2)


plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')   
plt.title('Original Image') 

plt.subplot(1, 3, 2)
plt.imshow(img_half, cmap='gray')
plt.title('Half Image')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(img_double, cv2.COLOR_BGR2RGB))
plt.title('Double Size Image')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# python _09_bitwise_scale.py (input arguments not fouund)