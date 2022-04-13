#!/usr/bin/python
# -*- coding: utf8 -*-

import imp
import rospy
from yh_tutorial_3.msg import yh_msg_3

def msgCallback(msg):
    
    rospy.loginfo("receive msg-stamp.secs = %d", msg.stamp.secs)
    
    rospy.loginfo("receive msg-stamp.nsecs = %d", msg.stamp.nsecs)
    
    rospy.loginfo("receive msg-data = %d", msg.data)

def listener():
    rospy.init_node("yh_sub_3", anonymous=True)
    rospy.Subscriber("yh_topic_3", yh_msg_3, msgCallback)

    rospy.spin()  

if __name__ == "__main__":
    listener()


"""
#include "ros/ros.h" // ROS 헤더파일
#include "yh_tutorial_3/yh_msg_3"  // my_msg 파일 헤더
                                    // 빌드 후 자동 생성

void msgCallback(const yh_tutorial_3::yh_msg_3::ConstPtr& msg)   // 메시지 콜백함수, 서브스크라이버가 메시지를 수신했을 때 동작하는 함수이다.
                                                                // 입력메시지로는 패키지 이름(topic_tutorial)의 메시지 이름(my_msg)을 받도록 되어있다.
{
    ROS_INFO("receive msg = %d", msg->stamp.sec); // stamp.sec를 표시한다.     - *msg.stamp.sec  ==  msg->stamp.sec ()
    ROS_INFO("receive msg = %d", msg->stamp.nsec); // stamp.nsec를 표시한다.
    ROS_INFO("receive msg = %d", msg->data); // data를 표시한다.
}

// 메인 함수
int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_sub_3"); // 노드 이름 초기화
    ros::NodeHandle nh; // ROS 시스템과 통신을 위한 노드 핸들 선언

    ros::Subscriber sub = nh.subscribe("yh_topic_3", 100, msgCallback);    // 서브스크라이버 선언
                                                                            // 패키지(topic_tutorial)의 메시지(my_msg)을 이용한 서브스크라이버(my_sub)를 작성한다.
                                                                            // 토픽명은 (my_topic)이며, 서브스크라이버큐(queue) 사이즈를 100으로 설정한다.
                                                                            // 콜백 함수는 (msgCallback)이다.

    ros::spin();    // 콜백 함수 호출을 위한 함수, 메시지가 수신되기를 대기
                    // 수신되었을 경우 콜백 함수를 호출한다.

    return 0;
}
"""