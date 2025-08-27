import cv2 as cv
import numpy as np

# Global variables
drawing = False
start_point = (-1, -1)
shape_type = None  # "circle" or "rectangle"
img = np.zeros((512, 512, 3), np.uint8)
img_copy = img.copy()  # for preview while dragging

# Mouse callback function
def drawFunction(event, x, y, flags, param):
    global drawing, start_point, shape_type, img, img_copy

# Left click down → circle
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        shape_type = "circle"

# Mouse middle button click → rectangle
    elif event == cv.EVENT_MBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        shape_type = "rectangle"

# Mouse move → draw preview
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            img = img_copy.copy()  # reset while dragging
            if shape_type == "circle":
                # distance formula to calculate radius sqrt(x1-x2)^2 + (y1-y2)^2)
                radius = int(((x - start_point[0])**2 + (y - start_point[1])**2)**0.5)
                cv.circle(img, start_point, radius, (255, 255, 255), -1)
            elif shape_type == "rectangle":
                cv.rectangle(img, start_point, (x, y), (0, 255, 0), 3)

# Left click up or right click up → finalize drawing
    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP:
        drawing = False
        if shape_type == "circle":
            # distance formula to calculate radius sqrt(x1-x2)^2 + (y1-y2)^2)
            radius = int(((x - start_point[0])**2 + (y - start_point[1])**2)**0.5)
            cv.circle(img, start_point, radius, (255, 255, 255), -1)
        elif shape_type == "rectangle":
            cv.rectangle(img, start_point, (x, y), (0, 255, 0), 3)
        img_copy[:] = img[:]  # update copy

# Bind mouse callback
cv.namedWindow('image')
cv.setMouseCallback('image', drawFunction)


# Main loop
while True:
    cv.imshow('image', img_copy)
    key = cv.waitKey(20) & 0xFF

    if key == 27:  # ESC
        break
    # elif key == ord('s'):  # Save image
    #     cv.imwrite("./img/saved_image.png", img)
    #     print("✅ Image saved!")

    if cv.getWindowProperty("image", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()

# python _12_Handling_event_2.py
