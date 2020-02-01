import argparse

import cv2

from imutils import flip

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

flip_horizontal = flip(image, "horizontal")
cv2.imshow("Horizontal flipped", flip_horizontal)

flip_vertical = flip(image, "vertical")
cv2.imshow("Vertical flipped", flip_vertical)

flip_horiz_and_vert = flip(image, "horizontal_and_vertical")
cv2.imshow("Horizontal and Vertical flipped", flip_horiz_and_vert)

cv2.waitKey(0)
