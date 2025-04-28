import cv2

#Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

# Command to open the webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    
    # required for Haar cascades
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # If faces are detected
    if len(faces) > 0:
        print("Face Detected!")
    else:
        print("No Face Detected.")
    
