import os
import fitz
import argparse
parser = argparse.ArgumentParser(description="Enumerate the pages in a PDF file")

def main():
    parser.add_argument("-i", "--input", help="the PDF file to enumerate")
    parser.add_argument("-o", "--output", help="the directory to write the output files to")
    parser.add_argument("-d", "--dpi", help="the DPI to use when rendering the pages", default=96, type=int)
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    pdf_file = fitz.open(args.input)

    for page in range(len(pdf_file)):
        print("Extracting page %d" % page)
        pix = pdf_file[page].get_pixmap(dpi=args.dpi)
        pix.save(args.output + "/page-%d.png" % page)

if __name__ == "__main__":
    main()