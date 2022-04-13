#include "ros/ros.h" 
#include "yh_sum/yh_sum_msg.h"  

// class MyClass
// {
//     public:
//         MyClass()
//         {
//             sub = nh.subscribe("yh_sum_topic", 100, &MyClass::msgCallback, this);
//         }
//         void msgCallback(const yh_sum::yh_sum_msg::ConstPtr &msg)
//         {
//             printf("%d\n", old_data + msg->data);
//             old_data = msg->data;
//         }

//     private:
//         ros::NodeHandle nh;
//         ros::Subscriber sub;
//         int old_data = 0;
// };


int old_data = 0;

void msgCallback(const yh_sum::yh_sum_msg::ConstPtr& msg)   
{
    printf("%d", old_data + msg->data);
    old_data = msg->data;
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_sum_sub"); 
    ros::NodeHandle nh; 

    ros::Subscriber sub = nh.subscribe("yh_sum_topic", 100, msgCallback);   
                                                                          
    // MyClass my_class;

    ros::spin();   
                    

    return 0;

}