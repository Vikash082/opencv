import cv2
import numpy as np


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


def rotation(image, angle, scale):
    h, w = image.shape[0], image.shape[1]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def resize(image, height=None, width=None, interpolation=cv2.INTER_AREA):
    actual_height, actual_width = image.shape[0], image.shape[1]
    dim = None

    if not height and not width:
        return image

    if not height:
        ratio = width / float(actual_width)    # ratio
        dim = (width, int(ratio * actual_height))
    elif not width:
        ratio = height / float(actual_height)
        dim = (int(ratio * actual_width), height)

    resized = cv2.resize(image, dim, interpolation=interpolation)
    return resized


def flip(image, direction):
    flip_direction = {
        "horizontal": 1,
        "vertical": 0,
        "horizontal_and_vertical": -1
    }
    return cv2.flip(image, flip_direction[direction])
