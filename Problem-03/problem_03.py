__author__ = 'Suvojit Manna'

# Write a program to remove the noise from the input images (SII_3_1, SII_3_2, SII_3_3, SII_3_4).

import cv2
from matplotlib import pyplot as plt
import numpy as np

images = ["SII_3_1", "SII_3_2", "SII_3_3", "SII_3_4"]
for pic in images:
    image = cv2.imread(pic + ".tif")
    cv2.imshow("Input " + pic, image)
    image = cv2.medianBlur(image, 5)
    cv2.imwrite("Output_" + pic + ".png", image)
    cv2.imshow("Output "+ pic, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()