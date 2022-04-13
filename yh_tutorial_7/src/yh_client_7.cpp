#include "ros/ros.h" // ROS 헤더 파일
#include "yh_tutorial_7/yh_srv_7.h"    // 서비스 헤더 파일
                                        // 빌드 후 생성
#include <cstdlib> // atoll 함수 사용을 위한 라이브러리

int main(int argc, char ** argv) // 메인 함수
{
    ros::init(argc, argv, "yh_client_7"); // 노드 이름 초기화

    // rosrun 패키지이름 노드이름 a b
    // argv = [노드이름, a, b]
    if (argc != 3) // 입력값 오류 처리
    {
        ROS_INFO("command : rosrun yh_tutorial_7 yh_client_7 arg1 arg2");
        ROS_INFO("arg1, arg2 : int64 number");

        return 1;
    }

    ros::NodeHandle nh; // 노드 핸들 선언

    // 서비스 클라이언트 선언
    // 서비스 클라이언트 (my_service_client)를 선언한다.
    // 서비스 이름은 (my_service)이고 패키지(service_tutorial)의 (my_srv)서비스 파일을 사용한다.
    ros::ServiceClient yh_service_client_7 = nh.serviceClient<yh_tutorial_7::yh_srv_7>("yh_service_7");

    yh_tutorial_7::yh_srv_7 srv;

    // 서비스 요청 값으로 노드 실행시 입력된 매개변수를 a, b에 저장한다.
    srv.request.a = atoll(argv[1]); 
    srv.request.b = atoll(argv[2]);

    if (yh_service_client_7.call(srv))
    {
        ROS_INFO("send srv, srv.request.a, b : %ld, %ld", srv.request.a, srv.request.b);
        ROS_INFO("receive srv, srv.request.result : %ld", srv.response.result);
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }

    return 0;
}