import sys
import cv2 as cv

def main(argv):
    filname = argv[0] if len(argv) > 0 else "./img/test2.jpg"

    #load the image
    src = cv.imread(cv.samples.findFile(filname))
    #check if image is loaded file
    if src is None:
        print("Error opening image!")
        return -1

    while 1:
        rows, cols, __channels = map(int, src.shape)

        cv.imshow('Pyramids Demo', src)

        k = cv.waitKey(0)
        if k == 27:
            break
        elif chr(k) == 'i':
            src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))
            print('** Zoom In: Image x 2')
        elif chr(k) == 'o':
            src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))
            print('** Zoom Out: Image / 2')

    cv.destroyAllWindows()
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])