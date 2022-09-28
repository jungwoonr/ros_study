#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int64

def publisher():
    pub = rospy.Publisher("my_cnt", Int64, queue_size=100)
    rospy.init_node("py_my_test_publisher")
    
    loop_rate = rospy.Rate(25)
    
    msg = Int64()
    msg.data = 0

    while not rospy.is_shutdown():
        for msg.data in range(0,101):
            pub.publish(msg)
            loop_rate.sleep()
            msg.data += 1

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass