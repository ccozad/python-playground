import cv2
import os
import sys
import argparse

import argparse
parser = argparse.ArgumentParser()

# Positional arguments can have short forms and long forms
parser.add_argument("-i", "--input", help="The input file to process")
parser.add_argument("-o", "--output", help="The output directory to write results to. Directory will be created if it doesn't exist.")
parser.add_argument("-s", "--stride", help="Capture one frame every <stride> frames", default=60, type=int)
parser.add_argument("-m", "--maxframes", help="Max number of frames to extract", default=1000, type=int)

# Optional flags use the store_true option to store a true value when specified
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show additional processing information")
args = parser.parse_args()
verbose = args.verbose

video = cv2.VideoCapture(args.input)

try:
    # Create the output directory
    if verbose:
        print("Checking to see if the output directory exists...")

    if not os.path.exists(args.output):
        if verbose:
            print("Output directory does not exist, creating it...")

        os.makedirs(args.output)
        print("Output directory created")
    else:
        if verbose:
            print("Output directory exists")
except OSError:
    sys.exit("Error creating output directory")

current_frame = 0
max_frames = args.maxframes * args.stride

while(current_frame < max_frames):
    ret, frame = video.read()

    if ret:
        if current_frame % args.stride == 0:
            name = args.output + "/frame_" + str(current_frame) + ".jpg"
            if verbose:
                print("Creating file " + name + "...")
                sys.stdout.flush()
            else:
                print(".", end="")
                sys.stdout.flush()
            
            cv2.imwrite(name, frame)

            if verbose:
                print("File created")
        
        current_frame += 1
    else:
        break

video.release()