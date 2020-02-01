import argparse

import cv2

# from ex1 import imutils
import imutils

# python translation.py --image ../../OpenCV_Basic_Exercises/images/image1.jpg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

shifted = imutils.translate(image, 25, 50)
cv2.imshow("Shifted Down and Right", shifted)

shifted_up_and_left = imutils.translate(image, -50, -90)
cv2.imshow("Shifted Up and Left", shifted_up_and_left)

shifted_down = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted_down)

cv2.waitKey(0)
