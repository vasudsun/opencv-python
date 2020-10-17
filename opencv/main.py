import numpy as np
import cv2
ball_cascade = cv2.CascadeClassifier('cascade.xml')
img = cv2.imread('image2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
balls = ball_cascade.detectMultiScale(gray, 1.01, 7)
for(x, y, w, h) in balls:
     img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
