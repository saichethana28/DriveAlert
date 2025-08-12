import cv2
import mediapipe as mp
import numpy as np
import pyttsx3

# Initialize mediapipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False,
                                  max_num_faces=1,
                                  refine_landmarks=True,
                                  min_detection_confidence=0.5,
                                  min_tracking_confidence=0.5)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Landmark indices for eyes and mouth (MediaPipe 468 points)
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
MOUTH = [13, 14]  # Upper and lower lip points

EAR_THRESHOLD = 0.25
EAR_CONSEC_FRAMES = 20
MAR_THRESHOLD = 0.6
MAR_CONSEC_FRAMES = 15

eye_counter = 0
yawn_counter = 0

def calculate_ear(landmarks, eye_indices):
    p1 = np.array(landmarks[eye_indices[1]])
    p2 = np.array(landmarks[eye_indices[5]])
    p3 = np.array(landmarks[eye_indices[2]])
    p4 = np.array(landmarks[eye_indices[4]])
    p5 = np.array(landmarks[eye_indices[0]])
    p6 = np.array(landmarks[eye_indices[3]])
    
    vertical1 = np.linalg.norm(p2 - p1)
    vertical2 = np.linalg.norm(p3 - p4)
    horizontal = np.linalg.norm(p5 - p6)
    
    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

def calculate_mar(landmarks):
    upper_lip = np.array(landmarks[MOUTH[0]])
    lower_lip = np.array(landmarks[MOUTH[1]])
    mar = np.linalg.norm(upper_lip - lower_lip)
    return mar

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)
    
    if results.multi_face_landmarks:
        mesh_points = results.multi_face_landmarks[0]
        landmarks = []
        for lm in mesh_points.landmark:
            x, y = int(lm.x * w), int(lm.y * h)
            landmarks.append((x, y))
        
        left_ear = calculate_ear(landmarks, LEFT_EYE)
        right_ear = calculate_ear(landmarks, RIGHT_EYE)
        min_ear = min(left_ear, right_ear)
        
        mar = calculate_mar(landmarks)
        
        # Display EAR and MAR
        cv2.putText(frame, f"EAR: {min_ear:.2f}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f"MAR: {mar:.2f}", (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Eye closure detection
        if min_ear < EAR_THRESHOLD:
            eye_counter += 1
            cv2.putText(frame, "Eyes Closed", (30, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            if eye_counter >= EAR_CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (30, 170),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                engine.say("Wake up! You are sleepy.")
                engine.runAndWait()
        else:
            eye_counter = 0
            cv2.putText(frame, "Eyes Open", (30, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Yawning detection
        if mar > MAR_THRESHOLD:
            yawn_counter += 1
            cv2.putText(frame, "Yawning", (30, 210),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            if yawn_counter >= MAR_CONSEC_FRAMES:
                cv2.putText(frame, "YAWN ALERT!", (30, 250),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                engine.say("You seem tired. Please take a break.")
                engine.runAndWait()
                yawn_counter = 0
        else:
            yawn_counter = 0
            
    else:
        # No face detected
        eye_counter = 0
        yawn_counter = 0
        cv2.putText(frame, "No face detected", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
