# Import Necessary library
import cv2
import numpy as np
import imutils


frame = cv2.imread('redball8.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
mask = cv2.dilate(mask, None, iterations=3)
cv2.imshow("MaskFrameInit", mask)
cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                       cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
center = None
cnt = cnts



for i in range (len(cnt)):
    (x,y),radius = cv2.minEnclosingCircle(cnt[i])
    center = (int(x),int(y))
    radius = int(radius)

    if radius >12 and radius < 15 and y < 580 :
       cv2.circle(frame,center,radius,(0,255,0),2)

cv2.imshow("MaskFrame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()