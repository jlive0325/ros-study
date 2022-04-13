#!/usr/bin/python
# -*- coding: utf-8 -*-

import imp
import turtle
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty
import math          # math.pi
import sys

class TurtleCircle():
    def __init__(self, radius):
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=100)
        self.client_teleport = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)
        self.client_clear = rospy.ServiceProxy("/clear", Empty)
        self.radius = radius

    def run(self):
        self.client_teleport(5.544445, 5.544445 + self.radius, 0)
        self.client_clear()
        msg = Twist()

        msg.linear.x = self.radius
        msg.angular.z = -1.0 

        loop_rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            self.pub.publish(msg)
            loop_rate.sleep()

if __name__ == "__main__":
    rospy.init_node("yh_turtle_circle")
    radius = float(sys.argv[1])
    turtle_circle = TurtleCircle(radius)
    turtle_circle.run()



""" def talker():
    rospy.init_node("yh_turtle_move")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=100)

    msg = Twist()
    loop_rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg.linear.x = 0
        msg.angular.z = math.pi / 1.5
        pub.publish(msg)
        loop_rate.sleep()

        msg.linear.x = 3
        msg.angular.z = 0
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass """
