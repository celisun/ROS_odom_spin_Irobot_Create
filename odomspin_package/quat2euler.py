# From quaternion to euler angles, publish converted euler to /odom_euler
# data range [0, 2*pi]
# Reference: https://answers.ros.org/question/69754/quaternion-transformations-in-python/

#!/usr/bin/env python

import roslib;
import rospy

import math
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32MultiArray 
from tf.transformations import euler_from_quaternion, quaternion_from_euler


rospy.init_node('quat2euler')   # ros node
rate = rospy.Rate(100)


roll = pitch = yaw = 0.   # initialize euler

pub = rospy.Publisher("odom_euler", Float32MultiArray, queue_size=1)   # create euler publisher
msgeuler = Float32MultiArray()


def callback(msg):
	global roll, pitch, yaw
    	orientation_q = msg.pose.pose.orientation   # get quaternion 
    	orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    	(roll, pitch, yaw) = euler_from_quaternion (orientation_list) # convert from qua to euler 
	
	yaw += math.pi    # convert yaw from [-pi, pi] to [0, 2*pi]

	msgeuler.data = [roll, pitch, yaw]	# set msg 
	pub.publish(msgeuler)   # publish msg
	


sub = rospy.Subscriber("odom", Odometry, callback)

while not rospy.is_shutdown():
	continue
