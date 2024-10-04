import cv2
import numpy as np

video_path = "C:\\Users\\YUG PATEL\\Downloads\\Solar info\\solartrack1.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    
    ret, frame = cap.read()
    
    
    if not ret:
        print("End of video or error in reading frame.")
        break
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    _, thresholded = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)

   
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    output_frame = frame.copy()
    cv2.drawContours(output_frame, contours, -1, (0, 255, 0), 2)  

   

    cv2.imshow('Video - Detected White Regions', output_frame)

    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()