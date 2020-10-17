import numpy as np
import cv2

blue = np.uint8([[[0, 0, 255]]])
hsvBlue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsvBlue)

lowerLimit = hsvBlue[0][0][0] - 10, 100, 100
upperLimit = hsvBlue[0][0][0] + 10, 255, 255
print("upper Limit")
print(upperLimit)
print("Lower Limit")
print(lowerLimit)
