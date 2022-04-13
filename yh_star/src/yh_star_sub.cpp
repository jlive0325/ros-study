#include "ros/ros.h" 
#include "yh_star/yh_star_msg.h"  
                                   

void msgCallback(const yh_star::yh_star_msg::ConstPtr& msg)   
{
    ROS_INFO("Number is = %d", msg->data);

    int num = msg->data;
    
    for (int i = 0; i < num/2; i++)
    {
        for (int j = 0; j < i+1; j++) printf("*");
        printf("\n");
    }
    for (int i = num/2; i < num ; i++)
    {
        for (int j = num; j > i; j--) printf("*");
        printf("\n");
    }


}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_star_sub"); 
    ros::NodeHandle nh; 

    ros::Subscriber sub = nh.subscribe("yh_star_topic", 100, msgCallback);   
                                                                          

    ros::spin();   
                    

    return 0;

}