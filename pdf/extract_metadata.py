import os
import fitz
import argparse
parser = argparse.ArgumentParser(description="Extract metadata from a PDF file")

def main():
    parser.add_argument("-i", "--input", help="the PDF file to examine")
    parser.add_argument("-e", "--extended", help="show extended metadata", action="store_true")
    args = parser.parse_args()

    pdf_file = fitz.open(args.input)
    metadata = pdf_file.metadata

    print("Metadata")
    for key, value in metadata.items():
        print(" - %s: %s" % (key, value))
    
    if args.extended:
        print("\nExtended metadata")
        extended_metadata = pdf_file.get_xml_metadata()
        print(extended_metadata)

if __name__ == "__main__":
    main()