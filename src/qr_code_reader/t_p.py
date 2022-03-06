#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import pyzbar.pyzbar as pyzbar
import cv2
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

#-*- coding:utf-8 -*-

cap = cv2.VideoCapture(0)

rospy.init_node('t_p')
pub = rospy.Publisher('counter', String, queue_size=10)
rate=rospy.Rate(2)

i = 0

toggle = 0
rem = ""
rem_ = ""
toggle2 = 0

while(cap.isOpened()):
  ret, img = cap.read()

  if not ret:
    continue

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
  decoded = pyzbar.decode(gray)

  for d in decoded: 
    x, y, w, h = d.rect

    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    text = '%s (%s)' % (barcode_data, barcode_type)
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    rem_ = rem
    rem = barcode_data
    if toggle2==0:
	rem_= barcode_data
	toggle2=1
    if toggle==0:
	#barcode_data = barcode_data.encode('utf-8')
	#barcode_data = barcode_data.decode('unicode_escape')
	print(type(barcode_data))
    	pub.publish(barcode_data)
	toggle=1

    if rem_ != rem:
	toggle=0
    

  cv2.imshow('img', img)

  key = cv2.waitKey(1)
  if key == ord('q'):
    break
  elif key == ord('s'):
    i += 1
    cv2.imwrite('c_%03d.jpg' % i, img)

cap.release()
cv2.destroyAllWindows()

"""

count=0
while not rospy.is_shutdown():
	pub.publish(count)
	count+=1
	rate.sleep()
"""
