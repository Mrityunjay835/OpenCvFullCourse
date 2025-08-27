# perform bitwise AND operation
# 🖼️ Bitwise 
# AND → keep common white parts
# OR → combine white parts
# XOR → keep only different parts
# NOT → invert (flip black/white)



# note👉: it only works with grayscale images.
# this program only shows the AND, OR, and XOR operations. Not saves the images.

#Must check _09_bitwise_resize.py to resize the images to the same size before running this code.



import cv2
import numpy as np
import matplotlib.pyplot as plt

# previously it takes binary1 --> after _09_bitwise_z1 and _09_bitwise_z1 ---> binary1_s
gray1 = cv2.imread('./img/binary1_s.png')
# previously it takes binary2 -->_09_bitwise_z1 and _09_bitwise_z2 -----> binary2_s
gray2 = cv2.imread('./img/binary2_s.png')

img1 = cv2.cvtColor(gray1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(gray2, cv2.COLOR_BGR2GRAY)


dest1 = cv2.bitwise_and(img2, img1, mask = None)
dest2 = cv2.bitwise_or(img2, img1, mask = None)
dest3 = cv2.bitwise_xor(img1, img2, mask = None)

plt.subplot(2, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('Image 1')

plt.subplot(2, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title('Image 2')

plt.subplot(2, 3, 3)
plt.imshow(dest1, cmap='gray')
plt.title('AND Operation')

plt.subplot(2, 3, 4)
plt.imshow(dest2, cmap='gray')
plt.title('OR Operation')

plt.subplot(2, 3, 5)
plt.imshow(dest3, cmap='gray')
plt.title('XOR Operation')

plt.show()

if cv2.waitKey(0) & 0xff == 27:
 cv2.destroyAllWindows()

 # python _09_bitwise.py (input arguments not fouund)
 # so we need to scale the images to the same size