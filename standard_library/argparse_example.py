# Alternatives to argparse include getopt and optparse 
# argparse is similar to other popular approaches in other languages
# so we'll use it as out library pf choice
import argparse
parser = argparse.ArgumentParser()

# Positional arguments can have short forms and long forms
parser.add_argument("-i", "--input", help="The input file or directory to process")
parser.add_argument("-o", "--output", help="The output file or directory to write results to")

# Optional flags use the store_true option to store a true value when specified
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show additional processing information")
args = parser.parse_args()
verbose = args.verbose

if verbose:
    print("Before printing the args")

print(args)

if verbose:
    print("After printing the args")