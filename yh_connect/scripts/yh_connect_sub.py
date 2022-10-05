#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import rospy
from std_msgs.msg import Float32

class ConnectSub:
    def __init__(self):
        self.sub = rospy.Subscriber("yh_cn_float", Float32, self.msgCallback)

    def msgCallback(self, msg):
        rospy.loginfo(msg.data)

if __name__ == "__main__":
    rospy.init_node("yh_connect_sub")
    connect_sub = ConnectSub()
    rospy.spin()
    