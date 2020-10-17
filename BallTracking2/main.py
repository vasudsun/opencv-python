
from __future__ import division
import numpy as np
import cv2
import imutils


redLower = (29, 86, 6)
redUpper = (64, 255, 255)

frame = cv2.imread('greenball.jpg')
frame = imutils.resize(frame, width=600)
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
# construct a mask for the color "green", then perform
# a series of dilations and erosions to remove any small
# blobs left in the mask
mask = cv2.inRange(hsv, redLower, redUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)


cv2.imshow('first mask', mask)


# find contours in the mask and initialize the current
# (x, y) center of the ball
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("CNTS: {}".format(cnts))
print("Type: {}".format(type(cnts)))
center = None
if len(cnts) > 0:

	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
# only proceed if the radius meets a minimum size
	if radius > 10:

		cv2.circle(frame, (int(x), int(y)), int(radius),(255, 255, 255), 2)
		cv2.circle(frame, center, 5, (0, 0, 255), -1)

cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()