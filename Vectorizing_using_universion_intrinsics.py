from __future__ import print_function
import sys
import cv2 as cv
import numpy as np

def main(argv):
    filename = argv[0] if len(argv) > 0 else 'test2.jpg'
    I = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    if I is None:
        print('Error opening image')
        return -1

    rows, cols = I.shape
    m = cv.getOptimalDFTSize(rows)
    n = cv.getOptimalDFTSize(cols)
    padded = cv.copyMakeBorder(I, 0, m - rows, 0, n - cols, cv.BORDER_CONSTANT, value=[0, 0, 0])

    planes = [np.float32(padded), np.zeros((padded.shape, np.float32))]
    complexI = cv.merge(planes)

    cv.dft(complexI, complexI)
    cv.magnitude(planes[0], planes[1], planes[0])
    magI = planes[0]

    cv.imshow("planes", complexI)
    cv.waitKey()

if __name__ == "__main__":
    main(sys.argv[1:])