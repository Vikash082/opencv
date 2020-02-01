import argparse

import cv2

from imutils import resize
# python resize.py --image ../../OpenCV_Basic_Exercises/images/image1.jpg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

sized_150 = resize(image, width=150)
cv2.imshow("Width 150", sized_150)

sized_height_50 = resize(image, height=50)
cv2.imshow("Height 50", sized_height_50)

cv2.waitKey(0)
