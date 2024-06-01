![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ccozad/python-playground)
![GitHub top language](https://img.shields.io/github/languages/top/ccozad/python-playground)
![GitHub](https://img.shields.io/github/license/ccozad/python-playground)
[![Run Python Tests](https://github.com/ccozad/python-playground/actions/workflows/pytest.yml/badge.svg)](https://github.com/ccozad/python-playground/actions/workflows/pytest.yml)

# Overview
 A collection of random Python solutions. If anything helps you here please give this repo a star.

 See commentary and other material on the [Think Create Repeat YouTube Channel](https://www.youtube.com/channel/UC1g9I6VprOjOn48jWC0mzmA)

# General Setup
It's recommended that you use a virtual environment to run each group of scripts. Each folder has its own requirements.txt file. the process for setting up your environment look like

 - Move to the topic folder
   - `cd <topic_folder>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

See this video for additional commentary on [Python Dev Environment Setup](https://www.youtube.com/watch?v=tk5WHjVuC4Q)

# Testing

 - *Create a virtual environment*
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - *Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - *Install dependencies*
   - On Mac: `pip install -r requirements.txt`
   - On Windoes: `pip install -r requirements.txt`
 - *Run tests*
   - `pytest -rA`

# Topics
Here's what you can find here:

## [Algorithms](/algorithms/)
- [Binary search](/algorithms/binary_search_client.py) an efficent search within sorted lists
- [Binary search tree](/algorithms/binary_tree.py) a specially organized binary tree that allows divide and conquer searches
- [Hamming distance](/algorithms/hamming_distance.py) Number of positions in which symbols differ for two equal length strings
- [Inorder tree traversal](/algorithms/binary_search_tree_walker.py) Traverse a binary search tree inorder to list nodes in sorted ascending order
- [Merge sort](/algorithms/merge_sort_client.py) an efficient way to sort a list
- [Reverse inorder tree traversal](/algorithms/binary_search_tree_walker.py) Traverse a binary search tree in reverse inorder to list nodes in sorted descending order

## [AWS](/aws/)
 - [DynamoDB](/aws/dynamodb/) fully managed NoSQL database service
   - [Create tables](/aws/dynamodb/create_tables.py) 
   - [List tables](/aws/dynamodb/list_tables.py) 
   - [Put items](/aws/dynamodb/put_items.py)
   - [Scan items](/aws/dynamodb/scan_items.py)

## [Azure](/azure/)
 - [Blob storage](/azure/blob_storage/) ubiqutous file storage on Azure
   - [Create container](/azure/blob_storage/create_container.py) 
   - [List containers](/azure/blob_storage/list_containers.py) 
   - [Upload blob](/azure/blob_storage/upload_blob.py) 
   - [List blobs](/azure/blob_storage/list_blobs.py) 
   - [Download blob](/azure/blob_storage/download_blob.py)
 - [Key vault](/azure/key_vault/) secret storage and crypto operations on Azure
   - [Set secret](/azure/key_vault/set_secret.py)
   - [Get secret](/azure/key_vault/get_secret.py)

## [Data Science](/data_science/)
 - [Load CSV into a pandas dataframe](/data_science/load_csv.py) 
 - [Group data and then find statistics for each group](/data_science/stats_by_group.py)

## [Games](/games/)
 - Boards
   - [2D grid](/games/boards/grid_2d.py) A simple representation of a 2D grid board that can be used for games like tic-tac-toe or checkers
   - [Tic-tac-toe board](/games/boards/tic_tac_toe_board.py) A board based on a 2D Grid that is specialized for the rules of tic-tac-toe
 - Cards
   - [Card deck](/games/cards/card_deck.py) A collection of cards that can be shuffled and dealt
   - [Card deck factory](/games/cards/card_deck_factory.py) A simplified way to construct various types of card decks
   - [Playing card](/games/cards/playing_card.py) A representation of a standard playing card
 - Clients
   - [Tic-tac-toe client](/games/game_clients/tic_tac_toe_client.py) Play tic-tac-toe using a simple command line client
 - Other
   - [Rubiks Cube Simulator](/games/rubiks_cube/rubiks-cube-2x2.py) Simulate moves on a 2x2 Rubik's cube

## [Interview Questions](/interview_questions/)
 - [Fizz buzz](/interview_questions/fizz_buzz.py) A test that makes sure you can apply simple rules and cover all cases
    - [Fizz buzz video tutorial](https://www.youtube.com/watch?v=8Kc7iAyuIkU)
 - [Largest common prefix](/interview_questions/largest_common_prefix.py) Consider what it means to have a common prefix and carfully enumerate the collection and individual characters of each word
 - [Reverse linked list](/interview_questions/reverse_linked_list.py) Reason about interactions with a data structure and carefully manipulate how the data is organized
 - [Reverse string](/interview_questions/reverse_string.py) Understand how to split and join on delimiters 
 - [Swap numbers](/interview_questions/swap_numbers.py) Write a few cryptic calculations to placate an interviewer trying to trick you
 - [Two sum](/interview_questions/two_sum.py) Simplify the problem space to find two numbers in a list that add up to a given number
 - [Valid parens](/interview_questions/valid_parens.py) Check for valid brackets sequences by tracking nesting using a stack

## [Math](/math/)
 - [Break even graph](/math/break_even_chart.py) Visualize where sales break even with costs
 - [Multiply matrices](/math/multiply_matrices.py) Solve a system of linear equations using matrices
 - [Pie chart](/math/pie_chart.py) Use a math plotting library to create a pie chart and save it to a file
 - [Plot Vectors](/math/plot_vectors.py) Use a math plotting library to plot and annotate vectors

## [PDF](/pdf/)
 - [Extract images from a pdf](/pdf/extract_images.py) Use pyMuPDF to extract imges from all pages
 - [Extract metadata from a pdf](/pdf/extract_metadata.py) Use pyMuPDF to extract metadata from all pages
 - [Extract pages from a pdf](/pdf/extract_pages.py) Use pyMuPDF to extract all pages and render the contents as an image
 - [Extract text from a pdf](/pdf/extract_text.py) Use pyMuPDF to extract text from all pages

## [Standard Library](/standard_library/)
 - [Base64 encode and decode](/standard_library/base64_example.py) A way to represent binary information using plain text
 - [JSON encode and decode](/standard_library/json_example.py) A way to share data structures across languages and systems
 - [Process command line arguments](/standard_library/argparse_example.py) Parse command line arguments using argparse
 - [Universally Unique ID](/standard_library/uuid_example.py) A standards based mechanism for generating unique ids
 - [Working with dates](/standard_library/datetime_example.py) Different ways to work with dates

## [Video](/video/)
 - [Extract frames from a video](/video/extract_video_frames.py) Use OpenCV to extract frames from a video
 - [Combine images into a video](/video/video_from_images.py) Use OpenCV to combine images into a video file
 - [List video properties](/video/video_properties.py) Use OpenCV to list properties such as frame rate, width, height and total frames

## [Web](/web/)
 - [Flask](/web/flask/)
   - [File uploads](/web/flask/file_uploads/app.py) A reference for uploading a file and saving it to a random name
   - [HTTP methods](/web/flask/http_methods/app.py) A compact reference for using common HTTP methods such as GET, POST, PATCH and DELETE
      - [HTTP methods video tutorial](https://www.youtube.com/watch?v=8pZwHItj0tg)
   - [SQL database](/web/flask/sql_database/) CRUD operations with a database over a REST API
 - Django
   - Coming soon!

# Support
 - How do I request a change?
   - Please submit an issue or a pull request
 - How fast will my request be added?
   - Probably not very fast for requests outside of a support package because this repo is maintained by a working professional
   - If you require fast, predictable responses, please purchase a support package
 - Can support packages be purchased?
   - Yes, various support packages can be purchased and customized for your needs. Support areas available include:
   - On demand support videos
   - 1:1 and team coaching
   - New features and other modifications

## License

Licensed under

 - MIT license
   ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)
