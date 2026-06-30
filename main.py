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

#For edge detection, it is better to make the image grey and blur it. So that's what we're gonna do.

grey_image = cv2.cvtColor(colour_image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(grey_image, (13,13), 0, 0)

#Now we can apply something called the Canny filter. As I understand it, it applies a matrix to each window of pixels to detect if that pixel is a corner or not.
thresh_low = 10
thresh_upp = 200
outline = cv2.Canny(blurred_image, thresh_low, thresh_upp)



cv2.imshow("scan", outline)
cv2.waitKey(0)
cv2.destroyAllWindows()