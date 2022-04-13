#!/usr/bin/python3
# -*- coding: utf8 -*-

import imp
import rospy
from yh_divisor.msg import yh_divisor_msg

def msgCallback(msg):

    rospy.loginfo("number is = %d", msg.data)

    num = msg.data
    s = " "

    # for i in range(1, num):
    #     if num % i == 0:
    #         s += str(i)
    #         s += " "
    # print(f"{num}의 약수는 : {s} 지롱")

    arr = list(filter((lambda x: num % x == 0), range(1,num + 1)))
    print(f"{num}의 약수는 {arr} 이지롱")

def listener():
    rospy.init_node("yh_divisor_sub", anonymous=True)
    rospy.Subscriber("yh_divisor_topic", yh_divisor_msg, msgCallback)

    rospy.spin()

if __name__ == "__main__":
    listener()