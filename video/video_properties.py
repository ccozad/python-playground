import cv2
import argparse

import argparse
parser = argparse.ArgumentParser()

# Positional arguments can have short forms and long forms
parser.add_argument("-i", "--input", help="The input file to process")

# Optional flags use the store_true option to store a true value when specified
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show additional processing information")
args = parser.parse_args()
verbose = args.verbose

video = cv2.VideoCapture(args.input)

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_rate = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

print(" - Width: ", width)
print(" - Height: ", height)
print(" - Frame Rate: ", frame_rate)
print(" - Frame Count: ", frame_count)


video.release()