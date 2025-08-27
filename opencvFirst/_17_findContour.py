#Contour is a curve joining all the continuous points along the boundary having the same
# color or intensity. The contours are very useful for shape analysis and object detection. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('./img/banImg.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny edge detection
canny = cv2.Canny(gray, 30, 200)

# Find contours
contours, hierarchy = cv2.findContours(canny,
                                       cv2.RETR_CCOMP,
                                       cv2.CHAIN_APPROX_NONE)

print("Number of Contours = ", len(contours))

# Draw contours on a copy of the image
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)

# Convert BGR → RGB for matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
contour_rgb = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

# Show results with matplotlib
titles = ['Original', 'Grayscale', 'Canny Edges', 'Contours']
images = [img_rgb, gray, canny, contour_rgb]

plt.figure(figsize=(10, 6))
for i in range(4):
    plt.subplot(2, 2, i+1)
    if i == 1 or i == 2:  # gray and canny are single channel
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# python _17_findContour.py
