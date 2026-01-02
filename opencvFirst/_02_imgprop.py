import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('./img/color_line.png')

print(f'Image shape: {img.shape}')
print(f'Image size: {img.size}')

pixal_val = img[100,100]
print(f'Pixel value at (10000,100): {pixal_val}')

# lets make 1/4 part black

for i in range(img.shape[0]//2):
    for j in range(img.shape[1]//2):
        img[i,j] = [0,0,0]


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
