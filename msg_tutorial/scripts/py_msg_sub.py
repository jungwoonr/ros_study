#!/usr/bin/python
# _*_ coding: utf-8 _*_
import rospy
from msg_tutorial.msg import Mymsg

def msgCallback(msg):
        rospy.loginfo("reseive msg: %d", msg.stamp.secs)
        rospy.loginfo("reseive msg: %d", msg.stamp.nsecs)
        rospy.loginfo("reseive msg: %d", msg.data)

def msg_listener():
    rospy.init_node("my_msg_sub")
    rospy.Subscriber("burger", Mymsg, msgCallback, queue_size=30)

    rospy.spin()

if __name__ == "__main__":
    msg_listener()
