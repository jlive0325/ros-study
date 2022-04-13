#include "ros/ros.h" 
#include "yh_sum/yh_sum_msg.h"

class MyClass
{
    public:
        MyClass();
        void run();

    private:
        ros::NodeHandle nh;
        ros::Publisher pub;
        int cnt = 0;
        yh_sum::yh_sum_msg msg;

};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_sum_pub"); 
    MyClass my_class;
    ros::Rate loop_rate(5);
    while (ros::ok())
    {    
        my_class.run();
        loop_rate.sleep();
    }
    // ros::NodeHandle nh; 
 
    // ros::Publisher pub = nh.advertise<yh_sum::yh_sum_msg>("yh_sum_topic", 100);

    // ros::Rate loop_rate(5);

    // yh_sum::yh_sum_msg msg;
    // int cnt = 0;

    // while (ros::ok())
    // {
    //     msg.stamp = ros::Time::now(); 
    //     msg.data = cnt; 
    //     ROS_INFO("send msg = %d", msg.stamp.sec); 
    //     ROS_INFO("send msg = %d", msg.stamp.nsec); 
    //     ROS_INFO("send msg = %d", msg.data); 
    //     cnt++;
    //     pub.publish(msg); 
    //     loop_rate.sleep(); 
    // }

    return 0;
}


MyClass::MyClass()
{
    pub = nh.advertise<yh_sum::yh_sum_msg>("yh_sum_topic", 100);
}

void MyClass::run()
{

    msg.stamp = ros::Time::now();
    msg.data = cnt;
    ROS_INFO("send msg = %d", msg.stamp.sec); 
    ROS_INFO("send msg = %d", msg.stamp.nsec); 
    ROS_INFO("send msg = %d", msg.data);
    pub.publish(msg);
    cnt++;
    // loop_rate.sleep();
    
}