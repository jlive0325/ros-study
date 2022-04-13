#include "ros/ros.h" 
#include "yh_divisor/yh_divisor_msg.h"  
                                   
void msgCallback(const yh_divisor::yh_divisor_msg::ConstPtr& msg)   
{
    ROS_INFO("Number is = %d", msg->data);

    int num = msg->data;

    // int divisor = 0;
    printf(" %d의 약수는 : ", num);

    for (int i = 1; i <= num; i++)
    {
        if (num % i == 0)
        {
            printf("%d, ", i);
        }
    }
    printf("\n");
    // printf("%d의 약수는 : %d", num, divisor);
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_divisor_sub"); 
    ros::NodeHandle nh; 

    ros::Subscriber sub = nh.subscribe("yh_divisor_topic", 100, msgCallback);   
                                                                          

    ros::spin();   
                    

    return 0;

}