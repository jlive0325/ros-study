/*
""" #!/usr/bin/python
# -*- coding: utf8 -*- 

import rospy
from yh_tutorial_4.msg import yh_msg_4

pub = rospy.Publisher("yh_topic_4_1", yh_msg_4, queue_size = 100)

def msgCallback(msg): 
    if msg.data % 5 == 0:
        pub.publish(msg)

def listener():

    rospy.init_node("yh_pub_sub_4", anonymous=True)
    rospy.Subscriber("yh_topic_4", yh_msg_4, msgCallback)
    rospy.spin()  

if __name__ == "__main__":
    listener()


# 힌트 -  전역변수, 콜백함수, 토픽 다름 """
*/


#include "ros/ros.h" // ROS 헤더파일
#include "yh_tutorial_4/yh_msg_4.h" 
                                   
ros::Publisher pub;

void msgCallback(const yh_tutorial_4::yh_msg_4::ConstPtr& msg) 
{
    if (msg->data % 5 ==0)
    {
        pub.publish(msg);

    }
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_pub_sub_4"); // 노드 이름 초기화
    ros::NodeHandle nh; // ROS 시스템과 통신을 위한 노드 핸들 선언

    pub = nh.advertise<yh_tutorial_4::yh_msg_4>("yh_topic_4_1", 100);
    ros::Subscriber sub = nh.subscribe("yh_topic_4", 100, msgCallback);  

    ros::spin();    // 콜백 함수 호출을 위한 함수, 메시지가 수신되기를 대기
                    // 수신되었을 경우 콜백 함수를 호출한다.

    return 0;

}



/*

class SubAndPub():






class SubAndPub
{
    public;     // SubAndPub - 멤버 접근 가능
                // 함수(메소드)
        SubAndPub() // 생성자
        {
            pub = nh.advertise<yh_tutorial_4::yh_msg_4>("yh_topic_4_1", 100);
            sub = nh.subscribe("yh_topic_4", 100, &SubAndPub::msgCallback, this);
        }

        void msgCallback(const yh_tutorial_4::yh_msg_4::ConstPtr& msg) 
        {
            if (msg->data % 5 ==0)
            {
                pub.publish(msg);

            }
        }



    private;    // 직접 접근 불가
                //변수

        yh_tutorial_4::yh_msg_4 msg;


        ros::Nodehandle nh;
        ros::Publisher pub;
        ros::Subscriber sub;

}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_pub_sub_4");

    SubSndPub sub_and_pub;

    ros::spin();

    return 0;

}