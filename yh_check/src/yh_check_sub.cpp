#include "ros/ros.h"
#include "yh_check/YhCheck.h"

/*
class MySub{
    public:
        // 함수
        MySub(void){
            sub_distance = nh.subscribe("check_distance", 10, &MySub::distanceCallback, this);
            sub_camera = nh.subscribe("check_camera", 10, &MySub::cameraCallback, this);
        }
    private:
        // 변수
        ros::NodeHandle nh;
        ros::Subscriber sub_distance;
        ros::Subscriber sub_camera;
        bool distance = true;
        bool camera = true;
};
*/

bool distance = true;
bool camera = true;

void distanceCallback(const yh_check::YhCheck::ConstPtr& msg){
    distance = msg->data;
    if(distance && camera){
        ROS_INFO("OK");
    }
}

void cameraCallback(const yh_check::YhCheck::ConstPtr& msg){
    camera = msg->data;
    if(distance && camera){
        ROS_INFO("OK");
    }
}

int main(int argc, char** argv){
    ros::init(argc, argv, "yh_check_sub");
    ros::NodeHandle nh;

    ros::Subscriber sub_distance = nh.subscribe("check_distance", 10, distanceCallback);
    ros::Subscriber sub_camera = nh.subscribe("check_camera", 10, cameraCallback);

    ros::spin();

    return 0;
}