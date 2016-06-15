__author__ = 'Suvojit Manna'

# Extract the rice objects from the input image (SII_5_3).

import cv2
from time import sleep
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("SII_5_3.tif")
cv2.imshow("Input", image)
image_org = image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.medianBlur(image, 5)
image_org = image
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (14, 14))
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
image = cv2.medianBlur(image, 5)
image = 255 - image
image = cv2.addWeighted(image, 1, image_org, 1, 0)
cv2.imwrite("Output_SII_5_3.png", image)
cv2.imshow("Output", image)
cv2.waitKey(0)