"""
Main steps to this project are as follows:

1. Detect the edges of the document
2. Use the edges of the document in the image the find the contour of the piece of paper being scanned. Basically try and find where the image stops being document and starts being background.
3. Apply a perspective transform of the image to get a scan-like view of the image.
"""

#Package imports:
import numpy as np
import cv2
import argparse
import imutils
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local


