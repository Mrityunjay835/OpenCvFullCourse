# color histogram
# To find the color histogram of an image, you need to 
# first convert the image to the HSV (Hue, Saturation, Value) color space.
#  Then, you can calculate the histogram of the Hue channel.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load the image
img = cv.imread('./img/lightbulb.jpg')

# Define colors (Blue, Green, Red channels in OpenCV)
color = ('b','g','r')

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
# Loop over each channel
for i,col in enumerate(color):
    # Calculate histogram for channel i  mask = None (consider all pixels) or no filter template
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    # Plot histogram
    plt.plot(hist, color = col)
    plt.xlim([0,256])  # Limit x-axis (pixel values from 0–255)
plt.title("Color Histogram")

plt.tight_layout()

# Show histogram
plt.show()

# python _15_color_hist.py