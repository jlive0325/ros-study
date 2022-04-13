#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#define _USE_MATH_DEFINES
#include <math.h>  // M_PI
#include "turtlesim/TeleportAbsolute.h"
#include "std_srvs/Empty.h"
#include <cstdlib>

class TurtleCircle
{

    public:
        TurtleCircle(double r)
        {
            pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
            client_clear = nh.serviceClient<std_srvs::Empty>("/clear");
            client_teleport = nh.serviceClient<turtlesim::TeleportAbsolute>("turtle1/teleport_absolute");
            radius = r;
        }

        void run(void)
        {
            turtlesim::TeleportAbsolute srv_teleport;
            srv_teleport.request.x = 5.544445;
            srv_teleport.request.y = 5.544445 - radius;
            srv_teleport.request.theta = 0;
            client_teleport.call(srv_teleport);

            std_srvs::Empty srv_clear;
            client_clear.call(srv_clear);

            ros::Rate loop_rate(1);
            geometry_msgs::Twist msg;
            msg.linear.x = radius * 3;
            msg.angular.z = 3;

            while (ros::ok())
            {
                pub.publish(msg);
                loop_rate.sleep();
            }
        
        }


    private:
        ros::NodeHandle nh;
        ros::Publisher pub;
        ros::ServiceClient client_clear;
        ros::ServiceClient client_teleport;
        double radius;


};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_turtle_circle");
    double radius = atof(argv[1]);
    TurtleCircle turtle_circle(radius);
    turtle_circle.run();

    return 0;

}











// int main(int argc, char **argv)
// {
//     ros::init(argc, argv, "yh_turtle_move");
//     ros::NodeHandle nh;

//     ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 100);
//     ros::Rate loop_rate(1);

//     geometry_msgs::Twist msg;
    
    

//     while (ros::ok())
//     {
//         msg.linear.x = 0;
//         msg.angular.z = M_PI / 1.5;
//         pub.publish(msg);
//         loop_rate.sleep();

//         msg.linear.x = 2;
//         msg.angular.z = 0;
//         pub.publish(msg);
//         loop_rate.sleep();
//     }
    

//     return 0;
// }





















// #include "ros/ros.h"
// #include "geometry_msgs/Twist.h"
// #include "turtlesim/TeleportAbsolute.h"
// #include "std_srvs/Empty.h"
// #include "math.h"
// #include <cstdlib>

// int main(int argc, char **argv)
// {
//     ros::init(argc, argv, "yh_turtle_move");
//     ros::NodeHandle nh;

//     ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 100);
//     ros::Rate loop_rate(1);
//     geometry_msgs::Twist msg;

//     int angle = M_PI;

//     msg.angular.z = angle;
//     msg.linear.x = 4;

//     while(ros::ok())
//     {   
//         // msg.angular.z = angle;
//         // msg.linear.x = 4;
//         pub.publish(msg);
//         loop_rate.sleep();
//     }

//     return 0;
// }

//////////////class구현 ////////////////////////

// class TurtleCircle
// {
//     public:
//         TurtleCircle(double r)
//         {
//             pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10); 
//             client_clear = nh.serviceClient<std_srvs::Empty>("/clear");
//             client_teleport = nh.serviceClient<turtlesim::TeleportAbsolute>("/turtle1/teleport_absolute");
//             radius = r;
//         }
//             void run(void)
//             {   
//                 turtlesim::TeleportAbsolute srv_teleport;
//                 srv_teleport.request.x = 5.54445;
//                 srv_teleport.request.y = 5.54445 - radius;
//                 srv_teleport.request.theta = 0;
//                 client_teleport.call(srv_teleport);

//                 std_srvs::Empty srv_clear;
//                 client_clear.call(srv_clear);

//                 ros::Rate loop_rate(1);
//                 geometry_msgs::Twist msg;
//                 msg.linear.x = radius * 3; 
//                 msg.angular.z = 3;

//                 while (ros::ok())
//                 {
//                     pub.publish(msg);
//                     loop_rate.sleep();
//                 }

//             }
//     private:
//         ros::NodeHandle nh;
//         ros::Publisher pub;
//         ros::ServiceClient client_clear;
//         ros::ServiceClient client_teleport;
//         double radius;

// };

// int main(int argc, char **argv)
// {

//     ros::init(argc, argv, "yh_turtle_circle");
//     double radius = atof(argv[1]); //정수를 더블 형으로 바꿔줌
//     TurtleCircle turtle_circle(radius);
//     turtle_circle.run();

//     return 0;
// }