import argparse

import cv2

import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

rotate_45_deg = imutils.rotation(image, 45, 1.0)
cv2.imshow("Rotated 45 degree", rotate_45_deg)

rotated_minus_90_deg = imutils.rotation(image, -90, 1.0)
cv2.imshow("Rotated by -90 degree", rotated_minus_90_deg)

rotate_180_degree = imutils.rotation(image, 180, 1.0)
cv2.imshow("Rotated by 180 degree", rotate_180_degree)

cv2.waitKey(0)
