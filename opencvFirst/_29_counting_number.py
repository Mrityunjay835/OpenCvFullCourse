import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for natural view (mirror effect)
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            h, w, _ = frame.shape
            landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]

            # Thumb (special case: compare x-coordinates)
            if landmarks[4][0] > landmarks[3][0]:  # Right hand
                finger_count += 1

            # Fingers (index, middle, ring, pinky) → compare y-coordinates
            if landmarks[8][1] < landmarks[6][1]:  # Index
                finger_count += 1
            if landmarks[12][1] < landmarks[10][1]:  # Middle
                finger_count += 1
            if landmarks[16][1] < landmarks[14][1]:  # Ring
                finger_count += 1
            if landmarks[20][1] < landmarks[18][1]:  # Pinky
                finger_count += 1

    # Show count on screen
    cv2.putText(frame, f"Fingers: {finger_count}", (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Show video
    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# python _29_counting_number.py