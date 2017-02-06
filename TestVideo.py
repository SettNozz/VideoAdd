import av
import librtmp
from glob import glob
from os import remove
from sys import argv
from subprocess import call
from os import listdir
from PIL import Image


fileName = argv[1]
imgName = argv[2]
x = int(argv[3])
y = int(argv[4])
nameOut = argv[5]
imagesPath = '/home/settnozz/PycharmProjects/vidTst/images/'
imageFramePath = '/home/settnozz/PycharmProjects/vidTst/frames/'
#imgChange = Image.open(imagesPath + imgName)
print('lalala')
container = av.open('http://127.0.0.1:1935/myapp/mystream')
print('rtmp://localhost/myapp/mystream opened')
video = next(s for s in container.streams if s.type == b'video')
print('after fideo=next')

for packet in container.demux(video):
    for frame in packet.decode():
        print(frame.to_image())#.save(imageFramePath + 'frame-%04d.jpg' % frame.index)


ar = listdir(imageFramePath)
files = filter(lambda z: z.endswith('.jpg'), ar)
filesList = sorted(files)
print(filesList)

def changePicture(x, y, imgInp, imgChange, nameFile):
    imgInp.paste(imgChange, (x, y))
    imgInp.save(imageFramePath + nameFile)


for i in filesList:
    imgInp = Image.open(imageFramePath + i)
    changePicture(x, y, imgInp, imgChange, i)


def makeVideo(nameOut):
    call(['ffmpeg', '-framerate', '13', '-i', imageFramePath + 'frame-%04d.jpg', nameOut])
    for file in glob.glob(imageFramePath + 'frame-*.jpg'):
        remove(file)

makeVideo(nameOut)
