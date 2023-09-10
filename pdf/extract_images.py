import os
import io
import fitz
from PIL import Image
import argparse
parser = argparse.ArgumentParser(description="Extract the images from each page a PDF file")

def main():
    parser.add_argument("-i", "--input", help="the PDF file to enumerate")
    parser.add_argument("-o", "--output", help="the directory to write the output files to")
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    pdf_file = fitz.open(args.input)

    for page in range(len(pdf_file)):
        images = pdf_file[page].get_images(full=True)

        if images:
            print("Found a total of %d images" % (len(images)))
        else:
            print("No images found")
        
        for image_index, img in enumerate(images, start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image = Image.open(io.BytesIO(image_bytes))
            image.save(args.output + "/page-%d-image-%d.%s" % (page, image_index, image_ext), format="%s" % image_ext)

if __name__ == "__main__":
    main()