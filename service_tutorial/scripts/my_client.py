#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from service_tutorial.srv import my_srv
import sys
 
def calculate_client(a, b):
    rospy.wait_for_service("my_service") # 서버가 죽었을때 대기
    try:
        my_service_client = rospy.ServiceProxy("my_service", my_srv)
        resp = my_service_client(a, b)

        return resp.result

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed : %s", e)

if __name__ == "__main__":
    rospy.init_node("my_client")
    if len(sys.argv) != 3:
        rospy.loginfo("usage : rosrun service_tutorial my_client.py a, b")
        # print("usage : rosrun service_tutorial my_client.py a, b")
        rospy.loginfo("a, b : int64 number")
        # print("a, b : int64 number")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    res = calculate_client(a, b)
    rospy.loginfo("send : a = %d, b = %d", a, b)
    rospy.loginfo("recevie : result = %d", res)

