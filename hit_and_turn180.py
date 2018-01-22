# A simple task of irobot create 2 for: 
# go straight forward, if obstacle detected at front (according to irobot bumper senosr), 
# make a 180 deg turn.

#!/usr/bin/env python

import roslib;
import rospy
import math

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray 
from ca_msgs.msg import Bumper


rospy.init_node('hit_and_turn180')
rate = rospy.Rate(5)

yaw = 0.  	  # track the current yaw
yaw_start = 0.    # initial yaw at turn
yaw_total = 0.    # how much turn has been made 
flag = False      # reverse the flag to get into turning state

# create publisher to speed 
pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)     
twist = Twist()

	
	

def callback_eu(msg):    # receive euler odom msg, set up yaw
	global yaw
	(x,y,z) = msg.data
	yaw = z


def callback(msg):
	global yaw, yaw_start, yaw_total
	global flag
	twist = Twist()
	
	# If in turn state, 
        # or should get ready for turns when obstacle detected at front	
	if flag or msg.is_light_center_left or msg.is_light_center_right \
		or msg.is_light_left or msg.is_light_front_left \
		or msg.is_light_front_right or msg.is_light_right:

		if not flag:         	 # not in turn state yet, turn on turn state, first time setting
			print "danger deteced!.."
			yaw_start = yaw
			flag = True           # reverse flag 
		else:  	 # if in turn state, calculate how much turn has been made
			if yaw < yaw_start: 
				yaw_total = yaw - yaw_start
			elif yaw > yaw_start: 
				yaw_total += yaw 

		print yaw_start, yaw, yaw_total 
		if yaw_total < math.pi:	          # turn  	
			print "I'm turning"
			twist.angular.z = -0.5
	 		pub.publish(twist)   
		else: 
			print "finish turns"
			twist.angular.z = 0.
			pub.publish(twist)

			flag = False             # reverse the flag, finish turning, 
			yaw_start, yaw_totoal = 0.        # clear preivous turn history
	
	else:
		print "go forward"
		twist.linear.x = 0.075
		twist.angular.z = 0.
		pub.publish(twist)	 # go forward




sub = rospy.Subscriber("odom_euler", Float32MultiArray, callback_eu)  # subcribe odom euler
sub = rospy.Subscriber("bumper", Bumper, callback)   # subscribe bumper for obstacle detection at front


while not rospy.is_shutdown():

	rate.sleep()



