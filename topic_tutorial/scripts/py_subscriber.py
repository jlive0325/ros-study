#!/usr/bin/python
# -*-coding:utf-8-*-

import imp
import rospy
from topic_tutorial.msg import my_msg

def msgCallback(msg):
    rospy.loginfo("send msg = %d", msg.stamp.secs)
    rospy.loginfo("send msg = %d", msg.stamp.nsecs)
    rospy.loginfo("send msg = %d", msg.data)

def listener():
    rospy.init_node("py_subscriber", anonymous=True)
    rospy.Subscriber("my_topic", my_msg, msgCallback)

    rospy.spin()

if __name__ == "__main__":
    listener()