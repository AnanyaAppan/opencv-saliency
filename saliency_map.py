# import the necessary packages
import argparse
import cv2
import numpy as np
import os
from data_loader import SaliencyDataset
from torch.utils.data import DataLoader
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image")
ap.add_argument('--dest_root', default='./data/maps/', help='Path to destination root', type=str)
args = vars(ap.parse_args())
path = args["image"]
# load the input image
# initialize OpenCV's static fine grained saliency detector and
# compute the saliency map
image = cv2.imread(path)
saliency = cv2.saliency.StaticSaliencyFineGrained_create()
(success, saliencyMap) = saliency.computeSaliency(image)
# if we would like a *binary* map that we could process for contours,
# compute convex hull's, extract bounding boxes, etc., we can
# additionally threshold the saliency map
# threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# show the images
# cv2.imshow("Image", image)
# cv2.imshow("Output", saliencyMap)
# cv2.imshow("Thresh", threshMap)
# cv2.waitKey(0)
root_dir = args["dest_root"]
directory = args["image"].split('/')[-2] + "/"
name = args["image"].split('/')[-1]
if not os.path.exists(root_dir + directory):
    os.makedirs(root_dir + directory)
cv2.imwrite(root_dir + directory + name,saliencyMap)