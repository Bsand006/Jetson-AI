import cv2

print(cv2.__version__)

dispW = 1280
dispH = 720
flip = 2
cv2.namedWindow('nanoCam')


camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=10/1 ! nvvidconv flip-method=' + str(flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(dispH) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
    
def click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event was:', event)
        print(x, ', ', y)
        
cv2.setMouseCallback('nanoCam', click)
    
while True:
   
   try:
    
       ret, frame = cam.read()
       cv2.imshow('nanoCam', frame)
       # cv2.moveWindow('nanoCam', 0, 0)
       if cv2.waitKey(1) > -1:
           break
   
   except KeyboardInterrupt:
       break

cam.release()
cv2.destroyAllWindows()
