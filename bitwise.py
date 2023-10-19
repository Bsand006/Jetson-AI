import cv2
import numpy as np

print(cv2.__version__)

dispW = 1280
dispH = 720
flip = 2
img1 = np.zeros((200, 200, 1), np.uint8)
img1[0:150, 0:120] = [255]

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method=' + str(flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(dispH) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

while True:
   
   try:
    
       ret, frame = cam.read()
       cv2.imshow('nanoCam', frame)
       cv2.moveWindow('nanoCam', 0, 0)
       cv2.imshow('img1', img1)
       cv2.moveWindow('img1', 1400, 0)
       if cv2.waitKey(1) > -1:
           break

   
   except KeyboardInterrupt:
       break

cam.release()
cv2.destroyAllWindows()
