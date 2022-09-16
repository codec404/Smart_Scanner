from pickle import TRUE
from re import IGNORECASE
import urllib.request as req
import numpy 
import cv2
import datetime
from PIL import Image
url = 'http://172.16.25.244:8080/shot.jpg'
while True:
    image = req.urlopen(url)
    imgBytes = bytearray(image.read())
    imgNumpy = numpy.array(imgBytes , dtype= numpy.uint8)

    frame = cv2.imdecode(imgNumpy , -1)
    cv2.imshow('Smarto Scanner', frame)
    
    tm = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    if cv2.waitKey(1) == ord('s') :
        imPil = Image.fromarray(frame)
        imPil.save(f'{tm} Scanned_Document.pdf')
