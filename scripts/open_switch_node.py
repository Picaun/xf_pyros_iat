#!/usr/bin/env python3
#coding:utf-8

import rospy
from std_msgs.msg import String
RESET_FLAG = False
FUNC_FLAG = False

def callback(data):
	global RESET_FLAG
	RESET_FLAG = True

def callback_fuc(data):# let "func_switch" pub to choice which control node to run
	global FUNC_FLAG
	FUNC_FLAG = True

def open_switch():
	global RESET_FLAG,FUNC_FLAG
	pub = rospy.Publisher('open_switch', String, queue_size=1)
	rospy.init_node('open_switch_node', anonymous=True)


	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		rospy.Subscriber("reset_switch",String,callback)
		rospy.Subscriber("func_switch_op",String,callback_fuc)
		if RESET_FLAG:
			RESET_FLAG = False
			FUNC_FLAG = False
			#rospy.signal_shutdown("reset!!")
		if FUNC_FLAG: # start this control function
			send_str = "1"
			rospy.loginfo(send_str)
			pub.publish(send_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		open_switch()
	except rospy.ROSInterruptException:
		pass

