# 2. Create a VideoCapture object with the camera index


import cv2

# Open webcam (0 = default camera, change to 1/2 if multiple webcams)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame not captured correctly
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Show the live video
    cv2.imshow("Webcam", frame)

    # Press 's' to save image, 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite("./vid/captured_image.jpg", frame)
        print("Image saved as captured_image.jpg")
    elif key == ord('q'):
        break

# Release the capture and close window
cap.release()
cv2.destroyAllWindows()


# python _22_video_capture.py