#include "ros/ros.h"
#include "msg_tutorial/Mymsg.h" // Mymsg 메세지 헤더 파일, 빌드 시 자동 생성

int main(int argc, char** argv){
    ros::init(argc, argv, "msg_publisher");
    ros::NodeHandle nh;

    // 퍼블리셔 선언
    // 퍼블리셔를 만드는 함수(nh.advertise)
    // 패키지(msg_tutorial)의 메세지파일(Mymsg)을 이용한 퍼블리셔(pub)를 만든다.
    // 토픽은 ("burger")이며, 퍼블리셔큐(queue) 사이즈는 (20)이다.
    ros::Publisher pub = nh.advertise<msg_tutorial::Mymsg>("burger", 20);

    ros::Rate loop_rate(2); // 루프 주기를 2Hz로 설정 1초에 2번

    msg_tutorial::Mymsg msg;
    int cnt = 0; // 정수 cnt에 0을 넣음

    while(ros::ok()){
        msg.stamp = ros::Time::now(); // 현재 시간을 msg의 stamp에 담는다
        msg.data = cnt; // cnt 변수의 값을 msg의 data에 담는다.
        ROS_INFO("send msg: %d", msg.stamp.sec); // stamp.sec를 출력
        ROS_INFO("send msg: %d", msg.stamp.nsec); // stamp.nsec를 출력
        ROS_INFO("send msg: %d", msg.data); // data를 출력
        pub.publish(msg); // pub이 msg를 퍼블리시
        loop_rate.sleep(); // 위에서 정한 주기에 따라 sleep
        cnt++;
    }

    return 0;

}