import cv2
print("OpenCV version:", cv2.__version__)
img = cv2.imread('./img/myimg.jpeg')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()