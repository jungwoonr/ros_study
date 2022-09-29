# ros_study
my first ros study

### 2022년 9월 27일 2일차 (토픽 통신)
- topic_tutorial 패키지에 src생성
- my_publisher, my_subscriber 노드 생성
- CMakeListsts.txt에서 빌드 후
- 터미널에서 실행

### 2022년 9월 28일 3일차 (토픽 통신)
- topic_tutorial 패키지에 python scripts 생성
- py_publisher.py, py_subscriber.py 노드 생성
- CMakeListsts.txt에서 빌드 후
- 터미널에서 실행

- topic_second 패키지 생성
- second_pub, second_sub, py_second.py, py_second.py 노드 생성
- CMakeListsts.txt에서 빌드 후
- 터미널에서 실행

- topic_test에서 과제1 진행

### 2022년 9월 29일 4일차 (서비스 통신)
- msg_tutorial 패키지 생성
- msg 디렉토리에 Mymsg.msg 생성
- msg_publisher, msg_subscriber, py_msg_pub.py, py_msg_sub.py 노드 생성
- CMakeListsts.txt에서 빌드 후
- 터미널에서 실행

## ROS 명령어
### roscore
- ROS Master 실행
- 노드를 켜기 전 가장 먼저 실행
```bash
    roscore
```

### rosrun
- 노드를 실행
- rosrun 패키지이름 노드이름
- 파이썬은 노드이름 맨 뒤에 .py 기입
```bash
    rosrun <패키지이름> <노드이름>
```

### 설정방법
- cd catkin_ws -> cd devel -> gedit ~/.bashrc

- 맨밑에서 밑의 소스들 추가 (설정)
- source ~/catkin_ws/devel/setup.bash
- alias cs='cd ~/catkin_ws/src'
- alias cw='cd ~/catkin_ws'
- alias cm='cd ~/catkin_ws && catkin_make'

### catkin_create_pkg
- 현재 위치한 작업 공간에 패키지를 생성하는 함수
- catkin_create_pkg 패키지이름 의존성
```bash
    catkin_create_pkg <패키지이름> <의존성1> <의존성2> ....
```
```bash
    catkin_create_pkg topic_tutorial roscpp rospy std_msgs
```

### chmod +x *
- 현재 위치아래 있는 파이썬 파일에 실행권한을 주는 함수.