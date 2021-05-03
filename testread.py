import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Read images
image=cv2.imread(args["image"])
cv2.imshow("image",image)
cv2.waitKey(0)