# Import Necessary library
import cv2
import numpy as np
import imutils
# Read Input image
frame = cv2.imread('redBall1.png')
# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])

# Threshold the HSV image to get only red colors

mask = cv2.inRange(hsv, lower_red, upper_red)
cv2.imshow("MaskFrame", mask)
cnts,hierarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(frame, cnts, -1, (0, 255, 0), 3)
#print(cnts)
#print len(cnts)
cnt = cnts

for i in range (len(cnt)):
    (x,y),radius = cv2.minEnclosingCircle(cnt[i])
    center = (int(x),int(y))
    radius = int(radius)


    if radius > 5 :
        print(radius)
        cv2.circle(frame,center,radius,(0,255,0),2)


cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()




