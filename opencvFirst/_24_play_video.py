import cv2

# Open video file
cap = cv2.VideoCapture("./vid/ImgVideo.avi")  # replace with your file name

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

screen_width = 1208
screen_height = 768

while True:
    ret, frame = cap.read()

   # Resize frame to fit screen (keep aspect ratio)
    frame = cv2.resize(frame, (screen_width, screen_height), interpolation=cv2.INTER_AREA)

    if not ret:
        print("End of video file reached")
        break

    # Show the video frame
    cv2.imshow("Video Playback", frame)

    # Press 'q' to exit playback
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# python _24_play_video.py
