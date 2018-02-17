# Geomtwo
A wanna-be Python package to handle planar geometry messages with ROS and Rospy.

## Installation
The package targets Ubuntu systems.
These instructions assume that you have ROS, Catkin and `python-catkin-tools` installed.

- Clone this repository in your catkin workspace
```
cd <your-catkin-workspace>/src
git clone https://github.com/adaldo/geomtwo
```
- Make and source
```
cd <your-catkin-workspace>
catkin build
source ./devel/setup.bash
```

## Provided messages
For now, the package provides the following messages:
- `Point`;
- `Vector`;
- `Pose`;
- `Transform`;
- `Twist`

## Demo
Type one of the following in a terminal:
- `roslaunch geomtwo test_point.launch`
- `roslaunch geomtwo test_pose.launch`

## Uninstall
- Just delete the `geomtwo` folder generated when cloning the repository.
- Write a mail to antonio.adaldo.89@gmail.com and let me know what went wrong.
