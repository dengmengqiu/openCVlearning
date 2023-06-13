import sys
import numpy as np
import cv2 as cv


def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)

def main(argv):
    filename = "img/tutorial_morph_lines_detection.png"
    if len(argv) > 0:
        filename = argv[0]

    src = cv.imread(filename, cv.IMREAD_COLOR)
    if src is None:
        print("open img error")
        return -1

    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src
    show_wait_destroy("src", src)

    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                            cv.THRESH_BINARY, 15, -2)
    show_wait_destroy("binary", bw)

    horizontal = np.copy(bw)
    vertical = np.copy(bw)

    horizontal_size = 60

    horizontal_structure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    horizontal = cv.erode(horizontal, horizontal_structure)
    horizontal = cv.dilate(horizontal, horizontal_structure)

    show_wait_destroy("horizontal", horizontal)


    rows = vertical .shape[0]
    vertical_size = rows // 30
    vertical_structure = cv.getStructuringElement(cv.MORPH_RECT, (1, vertical_size))

    vertical = cv.erode(vertical, vertical_structure)
    vertical = cv.dilate(vertical, vertical_structure)

    show_wait_destroy("vertical", vertical)

    # step 1: extract edges
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, \
                     3, -2)
    show_wait_destroy("edges", edges)

    #step 2: dilate edges
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    show_wait_destroy("dilate", edges)

    #stap 3: src.copyTo(smooth)
    smooth = np.copy(vertical)

    #step 4: blur smooth img
    smooth = cv.blur(smooth, (4, 4))

    #step 5: smooth.copyTo(src, edges)
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    #show final result
    show_wait_destroy("smooth - final", vertical)

    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv[1:])
