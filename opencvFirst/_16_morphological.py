# Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, Gradient etc also comes into play.

# 3A) EROSION :- The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object.

#3B) DILATION :- It is just like soil dilation, it increases the boundaries of foreground object.

# 3C) OPENING :- Opening is just another name of erosion followed by dilation. It is useful in removing noise.

# 3D) CLOSING :- Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

# 3E) MORPHOLOGICAL GRADIENT :- It is the difference between dilation and erosion of an image. The result will look like the outline of the object.

# 3F) TOP HAT :- It is the difference between input image and Opening of the image.

# 3G) BLACK HAT :- It is the difference between the closing of the input image and input image.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load image (binary or grayscale works best)
img = cv.imread('./img/banImg.png', 0)   # Change filename as per your image

# Apply threshold to make sure it's binary
_, binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Morphological operations
erosion = cv.erode(binary, kernel, iterations=1)
dilation = cv.dilate(binary, kernel, iterations=1)
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(binary, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)

# Titles and images
titles = ['Original', 'Erosion', 'Dilation', 'Opening',
          'Closing', 'Gradient', 'Top Hat', 'Black Hat']
images = [binary, erosion, dilation, opening, closing, gradient, tophat, blackhat]

# Plot all results
plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

# python _16_morphological.py