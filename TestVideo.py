import av
import glob
import os
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
imgChange = Image.open(imagesPath + imgName)
container = av.open(fileName)
video = next(s for s in container.streams if s.type == b'video')

for packet in container.demux(video):
    for frame in packet.decode():
        frame.to_image().save(imageFramePath + 'frame-%04d.jpg' % frame.index)


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
        os.remove(file)

makeVideo(nameOut)
