#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int64

def msgCallback(msg):
    rospy.loginfo("cnt: %s", msg.data)

def subscriber():
    rospy.init_node("py_my_test_subscriber")
    rospy.Subscriber("my_cnt", Int64, msgCallback, queue_size=100)

    rospy.spin()

if __name__ == "__main__":
    subscriber()