
# What is Bayer in OpenCV?
# Most digital cameras (especially cheap webcams, phone sensors, etc.) don’t capture full RGB at each pixel.
# Instead, they use a Bayer filter — a grid of color filters (Red, Green, Blue) placed over the sensor.
# Each pixel records only one color (R, G, or B), not all three.
# The missing colors are reconstructed later using a process called demosaicing (or debayering).


import cv2
import numpy as np

# Step 1: Read a normal color image
img = cv2.imread("./img/myimg.jpeg")

# Step 2: Convert to grayscale (simulate raw sensor data)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Simulate Bayer BG pattern by keeping only certain pixels
# OpenCV will interpret this as raw Bayer data
bayer = gray.copy()

# Step 4: Convert Bayer BG -> BGR
bgr_from_bayer = cv2.cvtColor(bayer, cv2.COLOR_BAYER_BG2BGR)

# Step 5: Show results
cv2.imshow("Original", img)
cv2.imshow("Simulated Bayer", bayer)
cv2.imshow("After Debayer (BGR)", bgr_from_bayer)

cv2.waitKey(0)
cv2.destroyAllWindows()
