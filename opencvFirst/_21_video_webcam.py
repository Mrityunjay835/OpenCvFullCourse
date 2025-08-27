# Video Capture
# using OpenCV to capture video from a webcam (livestream)
# If multiple cameras are connected, you can specify the camera index (0, 1, 2, etc.)
# cv.VideoCapture(0) opens the default camera (usually the first one) ... so on

#steps:
# 1. Import the necessary libraries
# 2. Create a VideoCapture object with the camera index
# 3. Check if the camera is opened successfully
# 4. Read the video frame by frame
# 5. Display the video frame
# 6. Exit when 'q' is pressed

import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
# Read and display video frames
while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        print("Error: Could not read frame.")
        break
    
    cv2.imshow('Video Frame', frame)  # Display the frame
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()  # Close all OpenCV windows

#python _21_video_webcam.py
