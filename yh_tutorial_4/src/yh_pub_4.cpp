/*
""" #!/usr/bin/python
# -*- coding: utf8 -*- 


import rospy
from yh_tutorial_4.msg import yh_msg_4

def talker():
    pub = rospy.Publisher("yh_topic_4", yh_msg_4, queue_size = 100)
    rospy.init_node("yh_pub_4", anonymous=True)
    loop_rate = rospy.Rate(10)
    cnt = 0
    msg = yh_msg_4()

    while not rospy.is_shutdown():
        msg.stamp = rospy.get_rostime()
        msg.data = cnt
        cnt += 1
        pub.publish(msg)
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass """
*/


#include "ros/ros.h" // ROS 헤더파일
#include "yh_tutorial_4/yh_msg_4.h" // my_msg 메시지 헤더파일
                                   // 빌드 후 자동 생성
// 메인함수
int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_pub_4"); // 노드 이름 초기화
    ros::NodeHandle nh; // ROS 시스템과 통신을 위한 노드 핸들 선언
 
    ros::Publisher pub = nh.advertise<yh_tutorial_4::yh_msg_4>("yh_topic_4", 100);  // 퍼블리셔 선언
                                                                                    // 패키지(topic_tutorial)의 메시지파일(my_msg)을 이용한
                                                                                    // 퍼블리셔(my_pub)을 작성한다. 토픽은 (my_topic)이며,
                                                                                    // 퍼블리셔큐(queue) 사이즈를 100개로 설정한다.

    ros::Rate loop_rate(10); // 루프 추가를 10Hz로 설정한다.

    yh_tutorial_4::yh_msg_4 msg;
    int cnt = 0;

    while (ros::ok())
    {
        msg.stamp = ros::Time::now(); // 현재 시간을 msg의 stemp에 담는다.
        msg.data = cnt; // cnt의 변수값을 msg의 data에 담는다.
        cnt++;
        pub.publish(msg); // my_pub의 msg를 퍼블리시한다.
        loop_rate.sleep(); // 위에서 정한 주기에 따라 sleep 한다.
    }

    return 0;
}


