import cv2

# Open webcam
cap = cv2.VideoCapture(0)
# Get resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define codec and create VideoWriter
out = cv2.VideoWriter('./vid/output.mp4',
                      cv2.VideoWriter_fourcc(*'MP4V'),
                      20.0,
                      (frame_width, frame_height))

recording = False  # Flag for recording state
print("Controls: 's' = start, 'p' = pause, 'q' = save & exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show the live video feed
    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        recording = True
        print("Recording started...")

    elif key == ord('p'):
        recording = False
        print("Recording paused...")

    elif key == ord('q'):
        print("Recording saved as output.mp4")
        break

    # Write frame if recording
    if recording:
        out.write(frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

# python _23_video_record.py
