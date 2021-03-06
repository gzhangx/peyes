import numpy as np
import cv2
import sys
import picamera
from picamera.array import PiRGBArray

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

imgx =  160
imgy = 120 
camera = picamera.PiCamera()
camera.resolution = (imgx, imgy)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(imgx, imgy))
import time

# allow the camera to warmup
time.sleep(0.1)
#video_capture = cv2.VideoCapture(0)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Capture frame-by-frame
    #ret, frame = video_capture.read()
    # grab an image from the camera
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rawCapture.truncate(0)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display the resulting frame
    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
