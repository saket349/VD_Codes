#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

PI = 3.14
speed = 2
radius = 1

def move():
	rospy.init_node('node_turtle_revolve', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size = 10)

	vel_msg = Twist()

	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.angular.z = speed/radius
	rospy.sleep(1)
	while not rospy.is_shutdown():
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
                
		while(current_distance <= 2*PI*radius):
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			current_distance = speed*(t1 - t0)

		vel_msg.linear.x = 0
		vel_msg.angular.z = 0

		velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:
		pass