#!/usr/bin/env python3
#coding:utf-8

import rospy
from std_msgs.msg import String

FUNC_FLAG = False

def callback_fuc(data):# let "func_switch" pub to choice which control node to run
	global FUNC_FLAG
	FUNC_FLAG = True

def reset_switch():
	global FUNC_FLAG
	pub = rospy.Publisher('reset_switch', String, queue_size=4)
	rospy.init_node('reset_switch_node', anonymous=True)

	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		rospy.Subscriber("func_switch_re",String,callback_fuc)
		if FUNC_FLAG:
			FUNC_FLAG = False
			rate_2 = rospy.Rate(50) # 50hz
			for i in range(1,20):
				send_str = "-1"
				rospy.loginfo(send_str)
				pub.publish(send_str)
				rate_2.sleep()
		rate.sleep()

if __name__ == '__main__':
	try:
		reset_switch()
	except rospy.ROSInterruptException:
		pass
