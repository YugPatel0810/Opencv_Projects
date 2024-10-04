import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    
    ret, frame = cap.read()
    
    
    if not ret:
        print("Error: Could not read frame.")
        break
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

    
    _, thresholded = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)

    
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
    output_frame = frame.copy()
    cv2.drawContours(output_frame, contours, -1, (0, 255, 0), 2)  

    
    cv2.imshow('Webcam Feed - Original', frame)
    cv2.imshow('Webcam Feed - Detected White Regions', output_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()