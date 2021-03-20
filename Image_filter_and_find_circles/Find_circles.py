import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('img.png')
output = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.5, 90)
if circles is not None:
	circles = np.round(circles[0, :]).astype("int")
	for (x, y, r) in circles:
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
	cv2.imshow("output", output)
	cv2.waitKey(0)

