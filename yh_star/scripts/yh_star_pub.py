#!/usr/bin/python3
# -*- coding: utf8 -*- 


import rospy
from yh_star.msg import yh_star_msg

def talker():
    pub = rospy.Publisher("yh_star_topic", yh_star_msg, queue_size = 100)
    rospy.init_node("yh_star_pub", anonymous=True)
    loop_rate = rospy.Rate(5)
    cnt = 0
    msg = yh_star_msg()

    while not rospy.is_shutdown():
        msg.stamp = rospy.get_rostime()
        msg.data = cnt
        rospy.loginfo("send msg = %d", msg.stamp.secs)
        rospy.loginfo("send msg = %d", msg.stamp.nsecs)
        rospy.loginfo("send msg = %d", msg.data)
        cnt += 1
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 