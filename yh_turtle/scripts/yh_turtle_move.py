#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle
import rospy
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node("yh_turtle_move")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=100)

    msg = Twist()
    msg.linear.x = 2
    loop_rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
