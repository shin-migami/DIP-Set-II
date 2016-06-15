__author__ = 'Suvojit Manna'

# Write a program in MATLAB to remove the noise from the input image (SII_5_1)

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("SII_5_1.tif")
cv2.imshow("Input", image)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Output", image)
cv2.imwrite("Output_SII_5_1.png", image)
cv2.waitKey(0)