# matching a specific part of image in a larger image

import cv2 as cv
import numpy as np

img = cv.imread('./img/myimg.jpeg')
template = cv.imread('./img/face.png')

# find the template in the image
w, h= template.shape[0], template.shape[1]
result = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result >= threshold) # getting coordinates of matched areas

for pt in zip(*loc[::-1]): # reversing the coordinates
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv.imshow('Detected', img)
cv.waitKey(0)
cv.destroyAllWindows()

#python _18_matching.py