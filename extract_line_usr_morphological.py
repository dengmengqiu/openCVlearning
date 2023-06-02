import numpy as np
import sys
import cv2 as cv

def main():
    src = cv.imread("five_stafff_line.png", cv.IMREAD_COLOR)

    if src is None:
        return -1

    cv.imshow("src", src)

    if (src.shape != 2) :
        gray = cv.cvtColor(src, cv.COLOR_BAYER_BG2GRAY)
    else:
        gray = src
    cv.imshow("gray", gray)

    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                cv.THRESH_BINARY, 15, -2)
    cv.imshow("binary", bw)

    horizontal = np.copy(bw)
    vertical = np.copy(bw)
    cols = horizontal.shape[1]
    horizontal_size = cols // 30

    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
