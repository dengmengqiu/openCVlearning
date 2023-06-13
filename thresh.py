import argparse

import cv2 as cv

window_name = "THreshold Demo"
trackbar_type = "Type:\n 0:Binary \n 2: Binary Inverted \n 2:\ Truncate \n 3: To Zero \n 4: To Zero Inverted"
trackbar_value = 'Value'
max_type = 4
max_value = 255
max_binary_value = 255

def Threshold_Demo(val):
    #0: Binary
    #1: Binary Inverted
    #2: Threshold to Truncated
    #3: Threshold to Zerp
    #4: Threashold to Zero Inverted
    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)
    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, threshold_type)
    cv.imshow(window_name, dst)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutoial.')
    parser.add_argument('--input', help='Path to input image.', default='img/test1.webp')
    args = parser.parse_args()

    src = cv.imread(cv.samples.findFile(args.input))
    if src is None:
        print("couldn't open the image", args.input)
        exit(0)

    # convert the image to Gray
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)


    cv.namedWindow(window_name)
    cv.createTrackbar(trackbar_type, window_name, 3, max_type, Threshold_Demo)
    cv.createTrackbar(trackbar_value, window_name, 0, max_value, Threshold_Demo)

    Threshold_Demo(0)

    cv.waitKey()
