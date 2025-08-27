# adding two images are similar to adding two matrices.
# if the two images are of different sizes, then the smaller image is padded with zeros.

#cv.add() function adds two arrays element-wise.

import cv2 as cv
import numpy as np  

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
added_image = cv.add(img1, img2)

# Display the original images and the added image
cv.imshow('Image 1', img1)
cv.imshow('Image 2', img2)
cv.imshow('Added Image', added_image)

# Wait for a key press and then destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()

#python _20_img_add_1.py