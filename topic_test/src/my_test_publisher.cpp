#include "ros/ros.h"
#include "std_msgs/Int64.h"

int main(int argc, char** argv){
    ros::init(argc, argv, "my_test_publisher");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::Int64>("my_cnt", 100);

    ros::Rate loop_rate(25);

    std_msgs::Int64 msg;
    msg.data = 0;

    while(ros::ok()){
        for(msg.data=0; msg.data <101; msg.data++){
            pub.publish(msg);
            loop_rate.sleep();
        }
    }
    return 0;
}