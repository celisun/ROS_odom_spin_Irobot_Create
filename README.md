# ROS odom spin  
Use ROS odometry messages to control accurate turns e.g. 180 deg on Irobot Create, can be used as the building block for navigations of various vehicles. 

Running scripts manipulates irobot to go forward and turn 180 deg if obstacle detected at front 

This package contains **a node that converts odometry from quaternion to euler form**, and publish to topic /odom_euler. 

**[Autonomous Robotics Lab](http://campusrover.org.s3-website-us-west-2.amazonaws.com)** 

@ Celi Sun  @ Nov, 2017  @ Brandeis University



## Dependencies

* ros kinetics
* [create autonomy](https://github.com/AutonomyLab/create_autonomy)
* math
* python


<img src="https://raw.githubusercontent.com/celisun/ROS_odom_spin_Irobot_Create/master/src/create-overview.png" width="180">
