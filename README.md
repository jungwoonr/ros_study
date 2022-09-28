# ros_study
my first ros study

### 2022년 9월 27일 2일차
- topic_tutorial 패키지에 src생성
- my_publisher, my_subscriber 노드 생성
- CMakeListsts.txt에서 빌드 후
- 터미널에서 실행

### 2022년 9월 28일 3일차
- topic_tutorial 패키지에 python scripts 생성
- py_publisher.py, py_subscriber.py 노드 생성
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
```bash
    rosrun <패키지이름> <노드이름>
```
### catkin_create_pkg
- 현재 위치한 작업 공간에 패키지를 생성하는 함수
- catkin_create_pkg 패키지이름 의존성
```bash
    catkin_create_pkg <패키지이름> <의존성1> <의존성2> ....
```
```bash
    catkin_create_pkg topic_tutorial roscpp rospy std_msgs
```
### <?> A,A,A </?>
-태그 함수
- <?> 열고 </?> 닫고
- 그사이에 내용 추가

### chmod +x *
- 현재 위치아래 있는 모든파일에 실행권한을 주는 함수.
