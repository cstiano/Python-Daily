# -*- coding: utf-8 -*-

import math

pi = math.pi
test_values = [pi/3.0,pi/4.0, pi/2.0, (2.0*pi)/3.0, (3.0*pi)/4.0, pi]

def rotate_angle(body_angle, objective_angle):
	result = (body_angle - objective_angle)
	print math.degrees(result)
	if (result>pi):
		result = -((2*pi)-result)
	elif (result<(-pi)):
		result = math.fabs(result+(2*pi))

	return result


def angle_objective(point1,point2):
	x = point2[0] - point1[0]
	y = point2[1] - point1[1]

	return math.atan2(y,x)

if __name__ == '__main__':
	print math.degrees(rotate_angle(math.radians(-150), math.radians(60)))
	print math.degrees(angle_objective((1,1),(2,2)))