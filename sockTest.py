#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import cv2
#from PIL import Image

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 9090))
sock.setblocking(False)
sock.listen(1)
fileName = 'newImage.jpg'

def maybeNewImage():
    try:
        conn, addr = sock.accept()
    except:
        dataTime = 100000
        return None, dataTime
    conn.setblocking(True)
    data = conn.recv(20000)
    newFile = open(fileName, 'w')
    newFile.write(data)
    newFile.close()
    imgRet = cv2.imread(fileName)
    dataTime = conn.recv(2048)
    conn.close()
    return(imgRet, dataTime)
