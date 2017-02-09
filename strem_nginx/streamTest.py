import cv2
import numpy as np
from PIL import Image

img2 = cv2.imread('/home/settnozz/python_stream/images/yellowCat.png')
cam2 = 'rtmp://localhost/myapp/mystream'

cap = cv2.VideoCapture()
cap.open(cam2)

while(True):
    ret, frame = cap.read()
    vis = cv2.add(frame, img2)
    cv2.imshow('frame', vis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
