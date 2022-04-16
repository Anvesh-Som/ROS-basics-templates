#include<ros/ros.h>
#include<std_msgs/Int32.h>
#include<std_msgs/Float32.h>

class s_class
	{
	ros::Subscriber sub_obj;
	ros::Publisher pub_obj;
	std_msgs::Int32 o_obj;
	std_msgs::Float32 i_obj;
//	ros::NodeHandle nh;
	public:
	s_class(int argc,char **argv)
		{
		ros::init(argc,argv,"pub_sub_class_node");
		}
	void callback(const std_msgs::Float32::ConstPtr& msg)
		{
		i_obj.data=msg->data;
		o_obj.data=2*(msg->data);
		ROS_INFO("Data subscribed= %f",msg->data);
		pub_obj.publish(o_obj);
		ROS_INFO("Data doubled after sub= %u",o_obj.data);
		}
	void pub_sub_func()
		{
		ros::NodeHandle nh;
		pub_obj=nh.advertise<std_msgs::Int32>("out_topic",5);
		sub_obj=nh.subscribe("in_topic",5,&s_class::callback,this);
		ros::spin();
		}
	};
int main(int argc,char **argv)
	{
	s_class obj(argc,argv);
	obj.pub_sub_func();
//	ros::init(argc,argv,"subscriber_class_node");
//	ros::NodeHandle nh;
//	ros::Subscriber sub=nh.subscribe("test_topic",5,&s_class::callback,&obj);
//	ros::spin();
	}

/* We can do it by two ways, either with subscribing in main, who's syntax is in comments
also, in that case we cannot define NodeHandle and subscriber object in private of class
Hence, The un-commented code is of that case along with using constructor
Apparently the initialization done in private happens before constructor, so can't include init inside constructor */ 
