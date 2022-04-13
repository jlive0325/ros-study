#include "ros/ros.h" // ROS 헤더파일
#include "yh_tutorial_7/yh_srv_7.h"    // 서비스 헤더 파일
                                        // 빌드 후 생성
// 서비스 요청이 있을 경우 실행되는 함수
// 서비스 요청은 req, 서비스 응답은 res로 설정


bool calculation(yh_tutorial_7::yh_srv_7::Request &req, yh_tutorial_7::yh_srv_7::Response &res)
{
    int max = 0;
    int min = 0;

    if (req.a > req.b)
    {
        max = req.a;
        min = req.b;
    } 
    else
    {
        max = req.b;
        min = req.a;
    }

    res.result = max - min;

    // 서비스 요청에 사용된 a, b 출력, 서비스 응답 result 값 출력
    ROS_INFO("request : a = %ld, b = %ld", req.a, req.b);
    ROS_INFO("response : %ld", res.result);

    return true;
}

int main(int argc, char** argv) // 메인 함수
{
    ros::init(argc, argv, "yh_server_7"); // 노드 이름 초기화
    ros::NodeHandle nh; // 노드 핸들 선언

    // 서비스 선언
    // 서비스 서버 (my_service_server)를 선언한다.
    // 서비스 이름은 (my_service)이고 요청이 왔을 때 (calculation)를 실행한다.
    // (service_tutorial)패키지의 (my_srv)서비스 파일을 이용한다.
    ros::ServiceServer yh_service_server_7 = nh.advertiseService("yh_service_7", calculation);

    ROS_INFO("Service Server Ready.");
    
    ros::spin(); // 서비스 요청 대기

    return 0;
}