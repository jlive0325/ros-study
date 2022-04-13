#!/usr/bin/python
# -*- coding: utf8 -*-

import imp
import turtle
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty
import math
import sys

class TurtleTriangle:
    def __init__(self, length):
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        # self.client_teleport = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)
        # self.client_clear = rospy.ServiceProxy("/clear", Empty)
        self.length = length

    def run(self):
        # self.client_teleport(5.544445 - self.length/2, 5.544445 - (math.sqrt(3) / 4 * self.length), 0)
        # self.client_clear()

        loof_rate = rospy.Rate(1)
        msg = Twist()
        
        while self.pub.get_num_connections() < 1:
            continue

        while not rospy.is_shutdown():
            for _ in range(3):
                msg.linear.x = self.length
                msg.angular.z = 0
                self.pub.publish(msg)
                loof_rate.sleep()
                
                msg.linear.x = 0
                msg.angular.z = math.pi / 1.5
                self.pub.publish(msg)
                loof_rate.sleep()

                
                
            # self.client_teleport(5.544445 - self.length/2, 5.544445 - (math.sqrt(3) / 4 * self.length), 0)
            # self.client_clear()

            

if __name__ == "__main__":
    rospy.init_node("yh_turtle_triangle")

    if len(sys.argv) != 2:
        print("erg error")
        sys.exit(1)

    turtle_triangle = TurtleTriangle(float(sys.argv[1]))
    turtle_triangle.run()
