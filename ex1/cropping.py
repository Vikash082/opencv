import argparse

import cv2

from imutils import flip

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)


cropped = image[30:120, 240:335]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
