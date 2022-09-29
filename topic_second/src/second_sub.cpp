#include "ros/ros.h" // ROS 헤더파일
#include "std_msgs/Int32.h" // Int32 메세지 헤더파일

void msgCallback(const std_msgs::Int32::ConstPtr& msg){
    ROS_INFO("count: %d", msg->data);
}

int main(int argc, char** argv){
    ros::init(argc, argv, "second_sub"); // 노드 이름 초기화
    ros::NodeHandle nh; // 노드 핸들 선언

    // 서브크라이버 선언
    // 패키지(std_msgs)의 메세지(Int32)를 이용한 서브크라이버(sub)를 선언한다.
    // 토픽은 ("my_second")이며, 서브크라이버큐(queue) 사이즈를 (100)으로 설정한다.
    // 콜백 함수는 (msgCallback)이다.
    ros::Subscriber sub = nh.subscribe("my_count", 100, msgCallback);

    // 콜백 함수 호출을 위한 함수, 메세지가 수신되기를 대기
    // 수신되었을 경우 콜백 함수를 호출한다.
    ros::spin(); // 대기하는 함수

    return 0;
}
