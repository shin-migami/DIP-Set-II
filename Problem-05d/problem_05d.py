__author__ = 'Suvojit Manna'

# Seperate the two types of blobs in the input image (SII_5_4)

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("SII_5_4.tif")
cv2.imshow("Input", image)
image_org = image
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (55, 55))
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (90, 90))
#image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
image = cv2.addWeighted(image_org, 1, image, 1, 0)
cv2.imshow("Output", image)
cv2.imwrite("Output_SII_5_4.png", image)
cv2.waitKey(0)
