import cv2
import os
import sys
import argparse

import argparse
parser = argparse.ArgumentParser()

# Positional arguments can have short forms and long forms
parser.add_argument("-i", "--input", help="The input directory to process")
parser.add_argument("-o", "--output", help="The output file to write results to")

# Optional flags use the store_true option to store a true value when specified
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show additional processing information")
args = parser.parse_args()
verbose = args.verbose

import re

images = [img for img in os.listdir(args.input) if img.endswith(".jpg")]
images.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
frame = cv2.imread(os.path.join(args.input, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(args.output, fourcc, 30, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(args.input, image)))

video.release()