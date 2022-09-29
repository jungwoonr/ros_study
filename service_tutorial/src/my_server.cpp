#include "ros/ros.h"
#include "service_tutorial/AddTwoInts.h" // 서비스 헤더파일
                                         // 빌드 시 생성

// 서비스 요청이 있을 경우 실행되는 콜백 함수
// 서비스 요청은 req, 서비스 응답은 res로 설정
bool add(service_tutorial::AddTwoInts::Request& req,
        service_tutorial::AddTwoInts::Response& res)
{
    res.result = req.a + req.b;
    ROS_INFO("request: a= %d, b= %d", req.a, req.b);
    ROS_INFO("response: result= %d", res.result);
    return true;
}

int main(int argc, char** argv){
    ros::init(argc, argv, "my_server");
    ros::NodeHandle nh;
    
    // 서비스 서버()를 선언
    // 서비스 이름은()이고, 요청이 왔을 때 ()를 실행
    // (service_tutorial) 패키지의 (AddTwoInts) 서비스 파일을 이용
    ros::ServiceServer my_server = nh.advertiseService("add_two_ints", add);

    ROS_INFO("Service Server Ready.");

    ros::spin();
    
    return 0;
}