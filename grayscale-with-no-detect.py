import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while True:
    
    ret, imageFrame = webcam.read()

    if not ret:
        break

    grayscaleFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
    
    _, bright_areas = cv2.threshold(grayscaleFrame, 200, 255, cv2.THRESH_BINARY)
   
    grayscale_3channel = cv2.cvtColor(grayscaleFrame, cv2.COLOR_GRAY2BGR)
    bright_areas_3channel = cv2.cvtColor(bright_areas, cv2.COLOR_GRAY2BGR)
   
    highlight_bright = cv2.addWeighted(grayscale_3channel, 0.8, bright_areas_3channel, 0.2, 0)
   
    cv2.putText(highlight_bright, "Bright areas are highlighted", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
   
    cv2.imshow("Bright Areas Detection", highlight_bright)
   
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()