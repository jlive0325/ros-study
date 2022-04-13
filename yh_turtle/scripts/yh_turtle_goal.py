#!/usr/bin/python
# -*- coding: utf8 -*-

from cgi import print_arguments
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MyTutle:
    def __init__(self):
        self.pub_cmd_vel = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=5)
        self.sub_pose = rospy.Subscriber("/turtle1/pose", Pose, self.update_pose)
        self.pose = Pose()
        self.loop_rate = rospy.Rate(10)

    def update_pose(self, msg):
        self.pose = msg
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        # (x1,y1) => (x2, y2)
        # (self.pose) => (goal_pose)

        diff_x = goal_pose.x - self.pose.x
        diff_y = goal_pose.y - self.pose.y

        return math.sqrt(diff_x*diff_x + diff_y*diff_y)

    def linear_vel(self, goal_pose, constant = 0.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return math.atan2((goal_pose.y - self.pose.y), (goal_pose.x - self.pose.x))

    def angular_vel(self, goal_pose, constant=8):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        goal_pose = Pose()

        goal_pose.x = float(input("x 좌표 어듸로 ? : "))
        goal_pose.y = float(input("y 좌표 어듸로 ? : "))

        tolerance = float(input("오차는 어느정도 ? : "))

        msg = Twist()

        while self.euclidean_distance(goal_pose) >= tolerance:
            msg.linear.x = self.linear_vel(goal_pose)
            msg.angular.z = self.angular_vel(goal_pose)

            self.pub_cmd_vel.publish(msg)
            self.loop_rate.sleep()
            
        msg.linear.x = 0
        msg.angular.z = 0
        self.pub_cmd_vel.publish(msg)

        print("도착해쒀~!!")

if __name__ == "__main__":
    rospy.init_node("yh_turtle_goal")
    try:
        my_turtle = MyTutle()
        my_turtle.move2goal()
    except rospy.ROSInterruptException:
        pass
        
