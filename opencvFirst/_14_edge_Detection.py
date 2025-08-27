# Edge Detection using Canny(John Canny) Edge Detector 
#step 1: Noise Reduction using Gaussian Filter
#step 2: Gradient Calculation using Sobel Filter
#step 3: Non-maximum Suppression
#step 4: Double Thresholding
#step 5: Edge Tracking by Hysteresis    


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 



img = cv.imread('./img/myimg.jpeg', 0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edges of original Image'), plt.xticks([]), plt.yticks([])
plt.show()

cv.imwrite('./img/myimg_edge.jpg', edges)
cv.waitKey(0)
cv.destroyAllWindows()
# python _14_edge_Detection.py