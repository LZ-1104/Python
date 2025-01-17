import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:/vscode/Python/Haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:/vscode/Python/MachineLearning-main/MachineLearning-main/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()    

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        gray = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,minSize=(30,30))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()