#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# encoding=utf8 
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

#-*- coding:utf-8 -*-

def callback(msg):
	print str(msg.data)
	print

rospy.init_node('t_s')

sub=rospy.Subscriber('counter',String, callback)

rospy.spin()
