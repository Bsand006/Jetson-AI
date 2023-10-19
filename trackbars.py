import cv2

print(cv2.__version__)

dispW = 1280
dispH = 720
flip = 2

def nothing():
    pass

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=10/1 ! nvvidconv flip-method=' + str(flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(dispH) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
cv2.namedWindow('nanoCam')
cv2.createTrackbar('xVal', 'nanoCam', 0, 500, nothing)
cv2.createTrackbar('yVal', 'nanoCam', 0, 500, nothing)
cv2.createTrackbar('radius', 'nanoCam', 0, 500, nothing)



while True:
   
   try:
       ret, frame = cam.read()
       xVal = cv2.getTrackbarPos('xVal', 'nanoCam')
       yVal = cv2.getTrackbarPos('yVal', 'nanoCam')
       radius = cv2.getTrackbarPos('radius', 'nanoCam')
       
       cv2.circle(frame, (xVal, yVal), radius, (255, 0, 0), -1)
       
       cv2.imshow('nanoCam', frame)
       #cv2.moveWindow('nanoCam', 0, 0)
       if cv2.waitKey(1) > -1:
           break
   
   except KeyboardInterrupt:
       break

cam.release()
cv2.destroyAllWindows()
