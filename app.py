from pickle import TRUE
from re import IGNORECASE
import urllib.request as req
import numpy 
import cv2
import datetime
from PIL import Image
url = 'http://172.16.14.156:8080/shot.jpg'
count = 0
while True:
    image = req.urlopen(url)
    imgBytes = bytearray(image.read())
    imgNumpy = numpy.array(imgBytes , dtype = numpy.uint8)

    frame = cv2.imdecode(imgNumpy , -1)
    frame_convert = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    frame_enhance = cv2.GaussianBlur(frame_convert , (5,5) , 0)
    frame_edge = cv2.Canny(frame_enhance , 30 , 50)
    contours , h = cv2.findContours(frame_edge , cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)

    if contours :
        max_cont = max(contours , key = cv2.contourArea)
        x , y , h , k = cv2.boundingRect(max_cont)
        cv2.rectangle (frame , (x,y) , (x+h , y+k) , (0,255,255) , 2)
        try :
                cv2.imshow('Smarto Scanner', frame)
                
                tm = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

                if cv2.waitKey(1) == ord('s') :
                    count += 1
                    imPil = Image.fromarray(frame_convert)
                    imPil.save(f'{tm} Scanned_Document_{count}.pdf')
        except Exception as e :
                pass
