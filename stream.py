import cv2
import sockTest
#import subprocess
import os

cam2 = 'rtmp://localhost/myapp/mystream'
#outStream = 'rtmp://localhost/strAds/mystreama'
cap = cv2.VideoCapture()
cap.open(cam2)
overlay = None
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('outstream.avi',fourcc, 20.0, (1092, 614))
counter = 0
countStop = 0

while(cap.isOpened()):
    counter +=1
    if counter == 10:
        print('cadr')
        os.system("gnome-terminal -e 'bash -c \"ffmpeg -re -i /home/settnozz/python_stream/outstream.avi -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv rtmp://live.twitch.tv/settnozz/live_64609648_vOa0jBYpxpYNbE0HoXjlf8ENxNDwLK; exec bash\"'")
        #subprocess.call(['ffmpeg', '-re', '-i', '/home/settnozz/python_stream/outstream.avi', '-c:v', 'libx264', '-preset', 'veryfast', '-maxrate', '3000k', '-bufsize', '6000k', '-pix_fmt', 'yuv420p', '-g', '50', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-ar', '44100', '-f', 'flv', 'rtmp://localhost/strAds/mystreama'])
    ret, frame = cap.read()
    if frame is None:
        continue


    maybeImage, countStop = sockTest.maybeNewImage()
    if maybeImage is not None:
        overlay = maybeImage
        counter = 0
        print(countStop)
    if overlay != None and counter < countStop:
        h2, w2 = overlay.shape[:2]
        frame[100:h2 + 100, 100:w2 + 100, :] = overlay
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
