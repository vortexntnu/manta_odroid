#!/usr/bin/python
import wiringpi as wpi
import time
import rospy
from std_msgs.msg import Bool

wpi.wiringPiSetup()

pub = rospy.Publisher('/mission_trigger', Bool, queue_size = 1)

rospy.init_node('trigger_node')

trigger_signal = True

def sendTrigger():
	pub.publish(trigger_signal)
	print "Trigger sent"

while not rospy.is_shutdown():
	time.sleep(0.05)

	# Read all pins
	#for pin in range(0, 30):
	#	adcValue = wpi.analogRead(pin)
	#	print (pin, adcValue)
	#	wpi.delay(100)

	adcValue = wpi.analogRead(29)

	if adcValue == 0:
		sendTrigger()
		wpi.delay(5000)
