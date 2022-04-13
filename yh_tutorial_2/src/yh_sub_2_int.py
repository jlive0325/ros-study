#!/usr/bin/python
# -*-coding:utf-8-*-

import imp
import rospy
from yh_tutorial_2.msg import yh_msg_2

def msgCallback(msg):
    if msg.stamp.secs % 2 != 0:
        rospy.loginfo("receive msg-stamp.secs = %d", msg.stamp.secs)
    if msg.stamp.nsecs % 2 != 0:
        rospy.loginfo("receive msg-stamp.nsecs = %d", msg.stamp.nsecs)
    if msg.data % 2 != 0:
        rospy.loginfo("receive msg-data = %d", msg.data)

def listener():
    rospy.init_node("yh_sub_2", anonymous=True)
    rospy.Subscriber("yh_topic_2", yh_msg_2, msgCallback)

    rospy.spin()

if __name__ == "__main__":
    listener()