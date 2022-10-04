#include "ros/ros.h"
#include "yh_dual/YhDualMsg.h"

void msgCallback(const yh_dual::YhDualMsg::ConstPtr& msg){
    ROS_INFO("receive msg: %d", msg->stamp.sec); // msg의 stamp의 sec를 출력
    ROS_INFO("receive msg: %d", msg->stamp.nsec); // msg의 stamp의 nsec를 출력
    ROS_INFO("receive msg: %d", msg->data); // msg의 data를 출력
}

int main(int argc, char** argv){
    ros::init(argc, argv, "yh_dual_int"); // 노드 이름 초기화
    ros::NodeHandle nh; // 노드 핸들 선언


    // 서브크라이버 선언
    // 패키지(msg_tutorial)의 메세지(Mymsg)를 이용한 서브크라이버(sub)를 선언한다.
    // 토픽은 ("burger")이며, 서브크라이버큐(queue) 사이즈를 (30)으로 설정한다.
    // 콜백 함수는 (msgCallback)이다.
    ros::Subscriber sub = nh.subscribe("yh_dual_topic", 30, msgCallback);

    // 콜백 함수 호출을 위한 함수, 메세지가 수신되기를 대기
    // 수신되었을 경우 콜백 함수를 호출한다.
    ros::spin(); // 대기하는 함수

    return 0;

}