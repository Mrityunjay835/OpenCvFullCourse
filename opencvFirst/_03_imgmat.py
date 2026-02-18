import cv2
import matplotlib.pyplot as plt
# Load the image
img = cv2.imread('./img/color_line.jpg',cv2.COLOR_GRAY2BGR)

plt.imshow(img)
plt.show()
cv2.destroyAllWindows()
