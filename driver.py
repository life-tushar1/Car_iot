import cv2
import numpy as np
import RPi.GPIO as GPIO
import pymysql
import sys
GPIO.setup(11,GPIO.IN)#ir1
GPIO.setup(12,GPIO.IN)#ir2
GPIO.setup(13,GPIO.IN)#press1
GPIO.setup(15,GPIO.IN)#press2

car=cv2.CascadeClassifier('car.xml')#for camera
cam=cv2.VideoCapture(0)

conn=pymysql.connect("localhost","root","","PARKING",autocommit=True)
cur=conn.cursor()


while True:
  ret, frame = cam.read()
  frame=imutils.resize(frame, width=min(500, frame.shape[1]))
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cars=car.detectMultiScale(gray,1.3,5)
  (update cars to data base entry)
  sql="insert into par(taken) values("+str(cars)+") WHERE sensor = 'cam'"
  if(GPIO.input(11)==1):
    sql="insert into par(taken) values(1) WHERE sensor = 'ir1'"
    cur.execute(sql)
  else:
    sql="insert into par(taken) values(0) WHERE sensor = 'ir1'"
    cur.execute(sql)
  if(GPIO.input(11)==1):
    sql="insert into par(taken) values(1) WHERE sensor = 'ir2'"
    cur.execute(sql)
  else:
    sql="insert into par(taken) values(0) WHERE sensor = 'ir2'"
    cur.execute(sql)
  if(GPIO.input(12)==1):
    sql="insert into par(taken) values(1) WHERE sensor = 'p1'"
    cur.execute(sql)
  else:
    sql="insert into par(taken) values(0) WHERE sensor = 'p1'"
    cur.execute(sql)
  if(GPIO.input(13)==1):
    sql="insert into par(taken) values(1) WHERE sensor = 'p2'"
    cur.execute(sql)
  else:
    sql="insert into par(taken) values(0) WHERE sensor = 'p2'"
    cur.execute(sql)
  if cv2.waitKey(1) & 0xFF == ord('q'):#opencv stuff
            break

  cam.release()
  cv2.destroyAllWindows()
  
