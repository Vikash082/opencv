from __future__ import print_function
import argparse
import cv2

# python ex1.py --image ../../OpenCV_Basic_Exercises/images/image1.jpg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print("width: %s pixels" % image.shape[1])
print("height: %s pixels" % image.shape[0])
print("channels: %s " % image.shape[2])


cv2.imshow("Image", image)
cv2.waitKey(0)
