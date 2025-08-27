import cv2 as cv
import numpy as np

#define mouse callback function to draw circle
def drawFunction(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 50, (255,255,255), -1)



#Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)

# cv.putText(img, "Press S to Save, ESC to Exit", (10, 150),
#            cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


# Create a window
cv.namedWindow('image')
# Bind the function to window so that mouse events are captured
cv.setMouseCallback('image', drawFunction)

# Display the image and wait for a keypress
while(1):
    # close the window with 'q' key or 27(ESC) key  
    cv.imshow('image', img)

    key = cv.waitKey(20) & 0xFF

    if cv.waitKey(20) & 0xFF == 27:
        break
    elif key == ord('s'):  # "S" key → save image
        cv.imwrite("saved_image.png", img)
        print("✅ Image saved as saved_image.png")
     # if window is closed with ❌ button, break
    if cv.getWindowProperty("image", cv.WND_PROP_VISIBLE) < 1:
        break
cv.destroyAllWindows()


# python _12_Handling_event_1.py