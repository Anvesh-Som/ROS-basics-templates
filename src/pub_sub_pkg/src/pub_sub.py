#! /usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32

class pub_sub(object):
	def __init__(self):
		self.Iobj=Int32()
		self.Fobj=Float32()
		self.Iobj.data=0
		self.Fobj.data=0
		rospy.init_node('pub_sub_node')
		self.pub_obj=rospy.Publisher('result_topic',Int32,queue_size=1)
		rospy.Subscriber('info_topic',Float32,self.callback)
#		rospy.spin()
		
	def callback(self,msg):	
		self.Fobj.data=msg.data
		rospy.loginfo("Subscribed data from info_topic = %f",self.Fobj.data)
#		self.Iobj.data=2*self.Fobj.data
#		self.pub_obj.publish(self.Iobj)
#		rospy.loginfo("Double of subscribed data is published =%u",self.Iobj.data)
#		if self.Fobj.data<20:
#			self.Iobj.data=-1
#			self.pub_obj.publish(self.Iobj)
#			rospy.loginfo("data < 20, so published to result_topic=%u",self.Iobj.data)
#		elif self.Fobj.data>20 and self.Fobj.data<30:
#			self.Iobj.data=0
#			self.pub_obj.publish(self.Iobj)
#			rospy.loginfo("data between 20&30, so published to result_topic=%u",self.Iobj.data)
#		elif self.Fobj.data>30:
#			self.Iobj.data=1
#			self.pub_obj.publish(self.Iobj)
#			rospy.loginfo("data > 30, so published to result_topic=%u",self.Iobj.data)
	def spin(self):
		rate=rospy.Rate(1)
		while not rospy.is_shutdown():
			self.Iobj.data=self.Fobj.data*2
			self.pub_obj.publish(self.Iobj)
			rospy.loginfo("Double of subscribed data is published =%u",self.Iobj.data)
			rate.sleep()
		
if __name__=='__main__':
#	try:
		obj2=pub_sub()
		obj2.spin()
		
#	except rospy.ROSInteruptException:
#		pass
