# Introduction

These examples show how to work with PDF document in Python

# Topics
 - [Extract images from a pdf](/pdf/extract_images.py) Use pyMuPDF to extract imges from all pages
 - [Extract metadata from a pdf](/pdf/extract_metadata.py) Use pyMuPDF to extract metadata from all pages
 - [Extract pages from a pdf](/pdf/extract_pages.py) Use pyMuPDF to extract all pages and render the contents as an image
 - [Extract text from a pdf](/pdf/extract_text.py) Use pyMuPDF to extract text from all pages
 

# Extract Images Usage

`python3 extract_images.py --input <path to pdf> --output ./output-images`

# Extract Metadata Usage

`python3 extract_metadata.py --input <path to pdf>`

# Extract Pages Usage

`python3 extract_pages.py --input <path to pdf> --output ./output --dpi 300`

# Extract Text Usage

`python3 extract_test.py --input <path to pdf> --output ./output`

# Resources

 - https://pymupdf.readthedocs.io/en/latest/index.html
 - https://opensource.adobe.com/dc-acrobat-sdk-docs/standards/pdfstandards/pdf/PDF32000_2008.pdf

**[Back to start](https://github.com/ccozad/python-playground)**