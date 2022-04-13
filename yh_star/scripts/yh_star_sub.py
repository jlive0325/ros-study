#!/usr/bin/python3
# -*- coding: utf8 -*-

import imp
import rospy
from yh_star.msg import yh_star_msg

def msgCallback(msg):

    rospy.loginfo("number is = %d", msg.data)

    num = msg.data
    star = ""

    for i in range(1, num//2 + 1):
        for j in range(i):
            star += "*"
        star += "\n"

    for i in range(num//2 + 1, num + 1):
        for j in range(num - i + 1):
            star += "*"
        star += "\n"

    print(star)


def listener():
    rospy.init_node("yh_star_sub", anonymous=True)
    rospy.Subscriber("yh_star_topic", yh_star_msg, msgCallback)

    rospy.spin()

if __name__ == "__main__":
    listener()