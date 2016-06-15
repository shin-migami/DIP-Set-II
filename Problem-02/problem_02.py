__author__ = 'Suvojit Manna'

# Write a program to reduce the salt-and-pepper noise from input image (SII_2_1).

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("SII_2_1.tif")
cv2.imshow("Input", image)
cv2.medianBlur(image, 5)
cv2.imshow("Output", image)
cv2.imwrite("Output_SII_2_1.png", image)
cv2.waitKey(0)