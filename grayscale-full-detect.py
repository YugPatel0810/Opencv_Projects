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
    
    # Add edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    _, thresholded = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a colored frame from the edge detection result
    colored_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(colored_frame, [largest_contour], -1, (0, 255, 0), 2)

    cv2.imshow('Webcam Feed - Original', frame)
    cv2.imshow('Webcam Feed - Edge Detection', colored_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()