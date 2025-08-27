# resize images for bitwise operations
# must be the same size and type
# otherwise it will give error
# so we will resize them to 300x300

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# make images the same size for bitwise operations
img1 = cv.imread('./img/binary1.png')
img2 = cv.imread('./img/binary2.png')

# resize images
resized_img1 = cv.resize(img1, (300, 300))
resized_img2 = cv.resize(img2, (300, 300))

# save as old_name_s.png
cv.imwrite('./img/binary1_s.png', resized_img1)
cv.imwrite('./img/binary2_s.png', resized_img2)

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(resized_img1, cv.COLOR_BGR2RGB))
plt.title('Resized Image 1')

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(resized_img2, cv.COLOR_BGR2RGB))
plt.title('Resized Image 2')

plt.show()

#exit
cv.waitKey(0)
cv.destroyAllWindows()  


# python _09_bitwise_z2.py (input arguments not fouund)