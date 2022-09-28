#include "ros/ros.h" // ROS 헤더파일
#include "std_msgs/Int32.h" // Int32 메세지 헤더파일

int main(int argc, char** argv){
    ros::init(argc, argv, "second_pub"); // 노드 이름 초기화
    ros::NodeHandle nh; // ROS 시스템과 통신을 위한 노드 핸들 선언

    // 퍼블리셔 선언
    // 퍼블리셔를 만드는 함수(nh.advertise)
    // 패키지(std_msgs)의 메세지파일(Int32)을 이용한 퍼블리셔(pub)를 만든다.
    // 토픽은 ("my_count")이며, 퍼블리셔큐(queue) 사이즈는 (100)이다. 
    ros::Publisher pub = nh.advertise<std_msgs::Int32>("my_count", 100);

    ros::Rate loop_rate(2); // 루프 주기를 2Hz로 설정
    
    std_msgs::Int32 msg;
    msg.data = 0; // msg의 data에 0을 넣음

    while(ros::ok()){
        pub.publish(msg); // pub이 msg를 퍼블리시한다.
        loop_rate.sleep(); // 위해서 정한 주기에 따라 sleep 한다.
        msg.data++; // 점점 1씩 증가
    }

    return 0;
}