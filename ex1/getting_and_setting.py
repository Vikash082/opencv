from __future__ import print_function
import argparse
import cv2

# python getting_and_setting.py --image \
# ../../OpenCV_Basic_Exercises/images/image1.jpg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: %s pixels" % image.shape[1])
print("height: %s pixels" % image.shape[0])
print("channels: %s " % image.shape[2])
cv2.imshow("Original", image)


corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 0, 255)
cv2.imshow("Updated", image)

# image[-128:, -250:] = (0, 255, 0)
image[:-128:-1, :-250:-1] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
