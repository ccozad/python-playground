import os
import fitz
import argparse
parser = argparse.ArgumentParser(description="Enumerate the pages in a PDF file")

def main():
    parser.add_argument("-i", "--input", help="the PDF file to enumerate")
    parser.add_argument("-o", "--output", help="the directory to write the output files to")
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    pdf_file = fitz.open(args.input)

    for page in range(len(pdf_file)):
        print("Extracting page %d" % page)
        text = pdf_file[page].get_text("blocks")
        with open(args.output + "/page-%d.txt" % page, "w") as f:
            output = []
            for block in text:
                output.append(block[4])

            f.write("\n".join(output))

if __name__ == "__main__":
    main()