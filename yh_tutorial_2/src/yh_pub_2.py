#!/usr/bin/python
# -*-coding:utf-8-*- 


import rospy
from yh_tutorial_2.msg import yh_msg_2

def talker():
    pub = rospy.Publisher("yh_topic_2", yh_msg_2, queue_size = 100)
    rospy.init_node("yh_pub_2", anonymous=True)
    loop_rate = rospy.Rate(5)
    cnt = 0
    msg = yh_msg_2()

    while not rospy.is_shutdown():
        msg.stamp = rospy.get_rostime()
        msg.data = cnt
        rospy.loginfo("send msg-stamp.secs = %d", msg.stamp.secs)
        rospy.loginfo("send msg-stamp.nsecs = %d", msg.stamp.nsecs)
        rospy.loginfo("send msg-data = %d", msg.data)
        cnt += 1
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass