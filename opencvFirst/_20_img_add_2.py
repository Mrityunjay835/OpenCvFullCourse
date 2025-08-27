#cv.addWeighted() function is used to add two images with different weights.

import cv2 as cv
import numpy as np  
import matplotlib.pyplot as plt

# Load two images   
img1 = cv.imread('./img/img1.png')
img2 = cv.imread('./img/img2.png')

# Check if images are loaded successfully
if img1 is None or img2 is None:
    print('Error: Image not loaded')
    exit()
# Resize images to the same size if they are no
if img1.shape != img2.shape:
    img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))
# Add the two images
added_image = cv.addWeighted(img1,0.7, img2,0.3,0)

image_list = [img1, img2, added_image]
titles = ['Image 1', 'Image 2', 'Added Image']

# Display the original images and the added image
plt.figure()
for i in range(len(image_list)):
    plt.subplot(1, 3, i + 1)
    plt.imshow(cv.cvtColor(image_list[i], cv.COLOR_BGR2RGB))
    plt.title(titles[i])

plt.tight_layout()
plt.show()
# Wait for a key press and then destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()

#python _20_img_add_2.py