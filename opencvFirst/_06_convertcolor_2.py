import cv2

img = cv2.imread('./img/myimg.jpeg')
resized = cv2.resize(img, (300, 400), 0.5, 0.5)
img1 = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY )
img2 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

# Displaying the image
cv2.imshow('original', img)
cv2.imshow('Gray', img1)
cv2.imshow('HSV', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# python _06_convertcolor_2.py