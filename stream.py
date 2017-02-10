import cv2
import sockTest

cam2 = 'rtmp://localhost/myapp/mystream'
cap = cv2.VideoCapture()
cap.open(cam2)
overlay = None


while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        print('no Frame', ret)
        continue
    
    maybeImage = sockTest.maybeNewImage()
    if maybeImage is not None:
        overlay = maybeImage
    	




    if overlay != None:
        h2, w2 = overlay.shape[:2]
        frame[:h2, :w2, :] = overlay
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
