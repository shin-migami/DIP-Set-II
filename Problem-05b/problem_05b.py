__author__ = 'Suvojit Manna'

# Write a program to extract the gradient parts from the input image (SII_5_2).

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("SII_5_2.tif")
cv2.imshow("Input", image)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Output", image)
cv2.imwrite("Output_SII_5_2.png", image)
cv2.waitKey(0)