# To create a Binary image we use the thresholding. In thresholding, we define the threshold for the pixel value where we compare the image pixel value with the threshold value. The steps are as follows:

# If the image is colored or in RGB format change it to grayscale image
# Define a threshold value.
# For each pixel present in the image, if the pixel value lies below the threshold value set that pixel value to 0 else 1.
# The result is a binary image.

import cv2
import matplotlib.pyplot as plt

# Step 1: Load the image
img = cv2.imread("./img/color_line.png")

# Step 2: Convert to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3.A: Apply Binary Threshold
# Anything above 127 becomes 255 (white), below becomes 0 (black)

#THIS COMMENTES LINE FOR INVERTED BINARY IMAGE
# _, binary = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)


# Step 3.B: Apply Otsu’s Thresholding
# The threshold value is automatically chosen
_, binary_otsu = cv2.threshold(
    gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# # Step 4: Show results
# cv2.imshow("Original", img)
# cv2.imshow("Gray", gray)
# cv2.imshow("Binary", binary_otsu)

#----------- USING MATPLOTLIB TO PLOT HISTOGRAM AND IMAGES -----------

# Step 4: Plot Histogram
plt.figure(figsize=(12,6))

# Histogram
plt.subplot(1,3,1)
plt.hist(gray_img.ravel(), 256, [0,256])
plt.axvline(_, color='r', linestyle='--', label=f"Otsu Threshold = {_:.0f}")
plt.title("Histogram of Grayscale Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

# Original Grayscale
plt.subplot(1,3,2)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

# Otsu Binary Result
plt.subplot(1,3,3)
plt.imshow(binary_otsu, cmap='gray')
plt.title("Binary Image (Otsu)")
plt.axis("off")

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# python _08_binary_img_generator.py

#note 
# THRESH_BINARY: above 127 → 255, else 0.
# THRESH_BINARY_INV: inverse of above.
# THRESH_TRUNC: above 127 → set to 127, else keep as is.
# THRESH_TOZERO: below 127 → 0, above → unchanged.
# THRESH_TOZERO_INV: inverse of above.

# ADAPTIVE_THRESH_MEAN_C: threshold = mean of neighborhood − C.

# ADAPTIVE_THRESH_GAUSSIAN_C: threshold = weighted sum (Gaussian) of neighborhood − C.