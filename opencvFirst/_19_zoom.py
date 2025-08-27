
#Image Pyramids
# Image pyramids are a way to represent an image at multiple resolutions. They are useful in
# computer vision tasks such as image processing, object detection, and image recognition.
# In OpenCV, image pyramids can be created using the `pyrUp` and `pyrDown` functions.


# Note 👉  that when we reduce the size of an image, information of the image is lost. Once, we
# scale down and if we rescale it to the original size, we lose some information and the
# resolution of the new image is much lower than the original one.

import sys
import cv2 as cv
filename = './img/lightbulb.jpg'
src = cv.imread(filename)
while 1:
    print ("press 'i' for zoom in 'o' for zoom out esc to stop")
    rows, cols, _channels = map(int, src.shape)
    cv.imshow('Pyramids', src)
    k = cv.waitKey(0)
    if k == 27:
        break

    elif chr(k) == 'i':
        src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))

    elif chr(k) == 'o':
        src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))

cv.destroyAllWindows()

# python _19_zoom.py
# press 'i' for zoom in 'o' for zoom out esc to stop