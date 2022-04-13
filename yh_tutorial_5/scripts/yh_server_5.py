#!/usr/bin/python
# -*- coding: utf8 -*-

import rospy
from yh_tutorial_5.srv import yh_srv_5, yh_srv_5Response

def caculation(req):
    rospy.loginfo("request : a = %d, b = %d", req.a, req.b)
    rospy.loginfo("response : %d", (req.a*req.b))

    return yh_srv_5Response(req.a*req.b)

def calculate_server():
    rospy.init_node("yh_server_5")
    yh_service_server_5 = rospy.Service("yh_service_5", yh_srv_5, caculation)
    rospy.loginfo("Service Server ready.")
    rospy.spin()

if __name__ == "__main__":
    calculate_server()