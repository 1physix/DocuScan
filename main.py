"""
Main steps to this project are as follows:

1. Detect the edges of the document
2. Use the edges of the document in the image the find the contour of the piece of paper being scanned. Basically try and find where the image stops being document and starts being background.
3. Apply a perspective transform of the image to get a scan-like view of the image.
"""

#Package imports:
import numpy as np
import cv2
import imutils

file = "img1.JPG"
colour_image = cv2.imread(file, 1)
cv2.imshow("scan", colour_image)

#For edge detection, it is better to make the image grey and blur it. So that's what we're gonna do.


grey_image = cv2.cvtColor(colour_image, cv2.COLOR_BGR2GRAY)



cv2.waitKey(0)
cv2.destroyAllWindows()