import cv2 as cv

img = cv.imread('./img/color_line.png')

print(img.shape)
print("img width : ",img.shape[0])
print("img height : ",img.shape[1])

# Titile
cv.putText(img, 'OpenCV', (230, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

# draw line/ horizontal line
cv.line(img,pt1= (0, img.shape[0]//2),pt2= (img.shape[1], img.shape[0]//2), color=(255, 0, 0),  thickness=2)

# draw rectangle
cv.putText(img, 'square', (45, 140), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
cv.rectangle(img, (260, 160),(170, 100), (0, 255, 0), 2)

#draw filled circle
cv.circle(img, (300, 300), 50, (0, 0, 255), -1)
cv.putText(img, 'circle', (45, 250), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv.imshow('Original Image', img)

cv.waitKey(0)
cv.destroyAllWindows()

# python run _11_draw_shapes.py