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
    vis = np.zeros((h1,w1, 3), np.uint8)
    vis[:h2, :w2, :3] = img2
    vis1 = cv2.addWeighted(frame, 1, vis, 1, 0)
    cv2.imshow('frame', vis1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
