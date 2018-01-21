import numpy as np
import cv2
import sys
import picamera

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

camera = picamera.PiCamera()
from picamera.array import PiRGBArray
rawCapture = PiRGBArray(camera)
import time

# allow the camera to warmup
time.sleep(0.1)
#video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    #ret, frame = video_capture.read()
	# grab an image from the camera
	camera.capture(rawCapture, format="bgr")
	image = rawCapture.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()