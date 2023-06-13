import sys
import cv2 as cv
import numpy as np

def main(argv)
    window_name = 'filter2D Demo'

    image_name = argv[0] if len(argv) > 0 else ""

    #loads an image
    src = cv.imre