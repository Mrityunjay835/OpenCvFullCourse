#image filtering = applying a small matrix (kernel) over the image to modify pixels for purposes like:

# 1.Reduce noise
# 2.Detect edges
# 3.Smooth or sharpen image
# 4.Highlight specific features

# 🔹 Common Image Filters in OpenCV
# 1.Averaging (cv2.blur) → smoothens image by averaging neighborhood pixels
# 2.Gaussian Blur (cv2.GaussianBlur) → weighted blur, better for noise reduction
# 3.Median Filter (cv2.medianBlur) → replaces pixel with the median of neighbors, removes salt & pepper noise
# 4.Bilateral Filter (cv2.bilateralFilter) → smoothens but keeps edges sharp
# 5.Sobel / Laplacian Filters → edge detection

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load as Image
img = cv.imread('./img/color_line.png', cv.IMREAD_COLOR)

# cv.imshow('Original Image', img)
# Convert to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
kernel = np.ones((3,3), np.float32) / 9


# Apply different filters
blur = cv.blur(gray_img, (5, 5))                  # Averaging
gaussian = cv.GaussianBlur(gray_img, (5, 5), 0)   # Gaussian Blur
median = cv.medianBlur(gray_img, 5)               # Median Filter
bilateral = cv.bilateralFilter(gray_img, 9, 75, 75)  # Bilateral Filter
Convolved = cv.filter2D(gray_img, -1, kernel)  # Mean Filter


# Show results side by side
titles = ['Original', 'Averaging', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter', 'Convolved(Mean Filter)']
images = [img, blur, gaussian, median, bilateral, Convolved]

plt.figure(figsize=(12, 8))

for i in range(6):
    plt.subplot(2, 3, i+1)   # 2 rows, 3 columns
    if i == 0:   # Original image is colored (BGR → RGB)
        plt.imshow(img[..., ::-1])  # Convert BGR to RGB 
        #                     or 
        # plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))      
    else:  # All other images are grayscale
        plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")


plt.tight_layout()
plt.show()


cv.imwrite('./img/color_line_filtered.jpg', img)
cv.waitKey(0)
cv.destroyAllWindows()

# python _13_image_filtring.py