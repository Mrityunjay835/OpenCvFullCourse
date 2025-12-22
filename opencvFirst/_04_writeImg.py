import cv2

#load the image
img = cv2.imread('./img/myimg.jpeg')

#display the image
cv2.imshow('Image', img)

#wait for a key press and destroy all windows
key = cv2.waitKey(0)

if(key == ord('s')): #if 's' is pressed, save the image
    cv2.imwrite('./img/myimg_copy.png', img)


cv2.destroyAllWindows()
