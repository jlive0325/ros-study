#!/usr/bin/python
# -*- coding: utf8 -*-

from re import MULTILINE
import rospy
from service_tutorial.srv import my_srv, my_srvResponse

PLUS = 1
MINUS = 2
MULTIPLICATION = 3
DIVISION = 4

def caculation(req):

    my_operator = rospy.get_param("calculation_method")

    if my_operator == PLUS:     
        res = req.a + req.b
    elif my_operator == MINUS:
        res = req.a - req.b
    elif my_operator == MULTIPLICATION:
        res = req.a * req.b
    elif my_operator == DIVISION:
        if req.b != 0:
            res = req.a / req.b
        else:
            res = 0
            error = "ERROR"

    rospy.loginfo("request : a = %d, b = %d", req.a, req.b)
    rospy.loginfo("response : %d", (res))

    return my_srvResponse(res, error)

def calculate_server():
    rospy.init_node("my_server")

    rospy.set_param("calculation_methood", PLUS)
    
    my_service_server = rospy.Service("my_service", my_srv, caculation)
    rospy.loginfo("Service Server ready.")
    rospy.spin()

if __name__ == "__main__":
    calculate_server()