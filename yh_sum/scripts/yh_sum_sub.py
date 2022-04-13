#!/usr/bin/python3
# -*- coding: utf8 -*-

import imp
import rospy
from yh_sum.msg import yh_sum_msg


class SumClass:
    def __init__(self) -> None:
        self.sub = rospy.Subscriber("yh_sum_topic", yh_sum_msg, self.msgCallback)
        self.old_data = 0

    def msgCallback(self, msg):
        sum = self.old_data + msg.data
        self.old_data = msg.data
        print(sum)



# sum = 0
# # old_data = 0

# def msgCallback(msg):

#     rospy.loginfo("number is = %d", msg.data)

#     num = msg.data
    
#     global sum

#     sum += num

#     print(sum)

    """
    global old_data
    print(old_data + msg.data)
    old_data = msg.data
    """


def listener():
    rospy.init_node("yh_sum_sub", anonymous=True)
    # rospy.Subscriber("yh_sum_topic", yh_sum_msg, msgCallback)
    sum_class = SumClass()
    rospy.spin()

if __name__ == "__main__":
    listener()
