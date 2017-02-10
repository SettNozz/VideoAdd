import cv2
import numpy as np
#from PIL import Image

img2 = cv2.imread('/home/settnozz/python_stream/images/yellowCat.jpg')
cam2 = 'rtmp://localhost/myapp/mystream'

cap = cv2.VideoCapture()
cap.open(cam2)

while(True):
    ret, frame = cap.read()
    h1, w1 = frame.shape[:2]
    h2, w2 = img2.shape[:2]
    frame[:h2, :w2, :] = img2
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
