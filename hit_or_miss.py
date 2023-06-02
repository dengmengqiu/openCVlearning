import cv2 as cv
import numpy as np

input_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 0, 0, 255],
    [0, 255, 255, 255, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 255, 255, 0],
    [0,255, 0, 255, 0, 0, 255, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")
input_image_complement = np.array((
    [255, 255, 255, 255, 255, 255, 255, 255],
    [255, 0, 0, 0, 255, 255, 255, 0],
    [255, 0, 0, 0, 255, 255, 255, 255],
    [255, 0, 0, 0, 255, 0, 255, 255],
    [255, 255, 0, 255, 255, 255, 255, 255],
    [255, 255, 0, 255, 255, 0, 0, 255],
    [255,0, 255, 0, 255, 255, 0, 255],
    [255, 0, 0, 0,  255, 255, 255, 255]), dtype="uint8")
kernel = np.array((
        [0, 1, 0],
        [1, -1, 1],
        [0, 1, 0]), dtype="int")
kernel_b1 = np.array((
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]), dtype="uint8")
kernel_b2 = np.array((
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]), dtype="uint8")

output_image = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel)
# output_image_b1 = cv.erode(input_image, kernel_b1, itertools=1)

rate = 50
kernel = (kernel + 1) * 127
# kernel = np.uint8(kernel)

show_input_image = cv.resize(input_image, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("Original", show_input_image)
cv.moveWindow("Original", 0, 200)

show_input_image_complement = cv.resize(input_image_complement, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("iOriginal_image_complement", show_input_image_complement)
cv.moveWindow("Original_image_complement", 0, 200)

print(kernel_b1)
print(type(kernel_b1))
output_image_b1 = cv.erode(input_image, kernel_b1)
output_image_b1 = cv.resize(output_image_b1, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("output_image_b1", output_image_b1)
cv.moveWindow("output_image_b1", 0, 200)

print(kernel_b2)
print(type(kernel_b2))
output_image_b2 = cv.erode(input_image_complement, kernel_b2)
output_image_b2 = cv.resize(output_image_b2, None, fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("output_image_b2", output_image_b2)
cv.moveWindow("output_image_b2", 0, 200)

output_image = cv.resize(output_image, None , fx = rate, fy = rate, interpolation = cv.INTER_NEAREST)
cv.imshow("Hit or Miss", output_image)
cv.moveWindow("Hit or Miss", 500, 200)

cv.imshow("~output_image_b1", output_image_b1 & output_image_b2)

cv.waitKey(0)
cv.destroyAllWindows()