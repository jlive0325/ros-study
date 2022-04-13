#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)

def msgCallback(msg):

    pub.publish(msg)

def listener():
    rospy.init_node("yh_turtle_keyboard")
    sub = rospy.Subscriber("/cmd_vel", Twist, msgCallback)
    rospy.spin()

if __name__ == "__main__":
    listener()
