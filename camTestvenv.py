import io
from picamera import PiCamera
import cv2 as cv
import numpy as np

stream = io.BytesIO()

camera = PiCamera()

camera.resolution = (320,240)
camera.capture(stream,format="jpeg")

buff = np.frombuffer(stream.getvalue(), dtype=np.uint8)

image = cv.imdecode(buff,1)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,5)

print("Found "+str(len(faces))+" face(s)")

for (x,y,w,h) in faces:
    cv.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

cv.imwrite('result_venv.jpg',image)
