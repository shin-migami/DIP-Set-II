__author__ = 'Suvojit Manna'

#Write a program to Implement the histogram equalization to the input images (SII_1_1 and SII_1_2)

import cv2
from matplotlib import pyplot as plt
import numpy as np

images = ["SII_1_1", "SII_1_2"]
for pic in images:
    image = cv2.imread(pic + ".tif")
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Input", image)
    plt.subplot(1, 2, 1), plt.hist(image.ravel(), 256, [0, 256])
    image = cv2.equalizeHist(image)
    cv2.imshow("Output", image)
    cv2.imwrite("Output_" + pic + ".png", image)
    plt.subplot(1, 2, 2), plt.hist(image.ravel(), 256, [0, 256])
    plt.show()
    cv2.waitKey(0)