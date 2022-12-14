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

### 2022년 9월 30일 5일차 
#### [과제 2 yh_star](./yh_star)

- for문 활용해서 별 찍기
- yh_star 패키지 생성
- yh_star_pub, yh_star_sub, yh_star_pub.py, yh_star_sub.py 노드 생성
- 빌드
- 실행

#### [과제 3 yh_service](./yh_service)
- yh_service 패키지 생성
- yh_server, yh_client, yh_server.py, yh_client.py 노드 생성
- 빌드
- 실행

## 2022년 10월 4일 6일차
### [param_tutorial](./param_tutorial)
- param_tutorial 패키지 생성
- calculate_server, calculate_client, calculate_server.py, calculate_client.py 노드 생성
- 빌드
- 실행
- 파라미터 서버 활용

### [과제4 yh_dual](./yh_dual)

### [과제5 yh_difference](./yh_difference)

## 2022년 10월 5일 7일차
### [과제6 yh_check](./yh_check)
- yh_check 패키지 생성

### [과제7 yh_connect](./yh_connect)

## 2022년 10월 6일 8일차
### [yh_turtle](./yh_turtle)
- yh_turtle 패키지 생성
- turtle_patrol, turtle_keyboard, turtle_clear, turtle_keyboard_clear, turtle_patrol.py, turtle_keyboard.py, turtle_clear.py, turtle_keyboard_clear.py 노드 생성
- [teleop_twist_keyboard 패키지 실습](#teleop_twist_keyboard)
- 빌드
- 실행

### [roslaunch 실습](#roslaunch)

---

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

### Parameter Server

- ROS Master에서 실행되고, 변수들을 담고 있는 서버
- ros::setParam(), ros::getParam(), rospy.set_param(), rospy.get_param() 등의 함수로 사용
- command line에서 rosparam으로 사용 가능
- rosparam list
  - 파라미터 서버의 모든 파라미터를 출력

```bash
    jungwoonr@ubuntu:~$ rosparam list
```
- rosparam get <파라미터 이름>
  - 파라미터의 값을 출력함

```bash
    jungwoonr@ubuntu: ~$ rosparam get <파라미터 이름>
```

- rosparam set <파라미터 이름> [파라미터 값]
   - 파라미터의 값을 지정함

```bash
    jungwoonr@ubuntu: ~$ rosparam set <파라미터 이름> [파라미터 값]
```
### [teleop_twist_keyboard 패키지](#teleop_twist_keyboard)
- 키보드 입력을 받아 /cmd_val 토픽의 geometry_msgs/Twist 메시지로 publish하는 노드
-설치
```bash
& sudo apt install ros_melodic-teleop-twist-keyboard
```
-실행
```bash
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

### [roslaunch](#roslaunch)
- roscore와 launch 파일에 있는 노드를을 실행시키는 명령
- launch 파일은 '패키지 디렉토리/launch'에 만든다.
- roslaunch 실행
```bash
$ roslaunch <패키지이름> <런치파일이름>
```
-launch 파일은 <launch></launcd> 태그 사이에 내용을 입력한다.
- node 태그는 패키지 이름, 노드 타입, 노드 이름을 입력한다.
- param 태그는 파라미터 이름, 값, 타입을 입력한다.

