#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sstream"

int main(int argc, char **argv)
{
	ros::init(argc, argv, "func_cl_node");// 初始化ros，向master注册一个叫“func_cl_node”的节点
	ros::NodeHandle n;              // 初始化一个句柄，就是将ROS实例化
	ros::Publisher chatter_pub = n.advertise<std_msgs::String>("func_switch_cl", 5);
  	//发布者注册一个叫“func_switch_cl”的话题，<消息类型>,5是消息队列大小
  	//消息队列相当于缓存消息，如果处理速度不够快的话消息会被保存在队列中
	ros::Rate loop_rate(10);
	for( int a = 1; a <= 10; a = a + 1 )
	{
		std_msgs::String msg;
		std::stringstream ss;
		ss << "act_close_node";
		msg.data = ss.str();
		chatter_pub.publish(msg);    // 发布该消息

		ros::spinOnce();
	 	loop_rate.sleep();
  	}
  	return 0;
}
