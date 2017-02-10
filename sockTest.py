#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import cv2
from PIL import Image

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('10.0.0.130', 9090))
sock.setblocking(False)
sock.listen(1)


def maybeNewImage():
    try:
        conn, addr = sock.accept()
    except:
        return None
    conn.setblocking(True)
    data = conn.recv(4096)
    imgRet = cv2.imread(data)
    conn.close()
    return(imgRet)
