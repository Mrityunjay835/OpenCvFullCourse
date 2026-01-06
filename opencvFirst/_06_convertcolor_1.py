import cv2

img = cv2.imread('./img/color_line.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Gray image', gray_img)
cv2.imwrite('./img/gray_img.png', gray_img)

img2 = cv2.imread('./img/gray_img.png',cv2.IMREAD_GRAYSCALE)
color_img = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
cv2.imshow('Gray image', color_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
