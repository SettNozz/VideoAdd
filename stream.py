import cv2
import numpy as np
from PIL import Image

img2 = cv2.imread('/home/settnozz/python_stream/images/cat.jpg')
cam2 = 'rtmp://localhost/myapp/mystream'

cap = cv2.VideoCapture()
cap.open(cam2)

while(True):
    ret, frame = cap.read()
    h1, w1 = frame.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
    vis[:h1, :w1, :3] = frame
    vis[:h2, w1:w1 + w2, :3] = img2
    cv2.imshow('frame', vis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
