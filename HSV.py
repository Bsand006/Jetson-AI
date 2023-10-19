import cv2
import numpy as np

def nothing():
    pass

dispW = 1280
dispH = 720
flip = 2

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', 1400, 0)

cv2.createTrackbar('hueLower', 'Trackbars', 50, 179, nothing)
cv2.createTrackbar('huehigher', 'Trackbars', 100, 179, nothing)
cv2.createTrackbar('satLower', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('satHigher', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('valLower', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('valHigher', 'Trackbars', 100, 255, nothing)


camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method=' + str(flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(dispH) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

while True:
   try:
       ret, frame = cam.read()
       cv2.imshow('nanoCam', frame)
       cv2.moveWindow('nanoCam', 0, 0)
      
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       
       if cv2.waitKey(1) > -1:
           break
   
   except KeyboardInterrupt:
       break

cam.release()
cv2.destroyAllWindows()
