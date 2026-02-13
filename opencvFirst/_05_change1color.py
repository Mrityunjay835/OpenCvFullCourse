# import lib
import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread("./img/color_line.png")

print(f"Image shape: {img.shape}")
print(f"Image size: {img.size}")
pixal_val = img[100, 100]
print(f"Pixel value at (10000,100): {pixal_val}")

b, g, r = cv2.split(img)
# print('red channel, green channel, blue channel', r, g, b)

img[:, :, 0] = 0 # set blue channel to zero
img[:, :, 1] = 0 # set green channel to zero

# Everything is red now
cv2.imshow("Image", img)
cv2.imwrite("./img/color_line_red.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
