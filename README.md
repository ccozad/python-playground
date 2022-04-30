![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ccozad/python-playground)
![GitHub top language](https://img.shields.io/github/languages/top/ccozad/python-playground)
![GitHub](https://img.shields.io/github/license/ccozad/python-playground)
[![Run Python Tests](https://github.com/ccozad/python-playground/actions/workflows/pytest.yml/badge.svg)](https://github.com/ccozad/python-playground/actions/workflows/pytest.yml)

# Overview
 A collection of random Python solutions. If anything helps you here please give this repo a star.

# General Setup
It's recommended that you use a virtual environment to run each group of scripts. Each folder has its own requirements.txt file. the process for setting up your environment look like

 - *Move to the topic folder*
   - `cd <topic_folder>`
 - *Create a virtual environment*
   - `python3 -m venv .venv`
 - *Activate the virtual environment on Mac*
   - `source .venv/bin/activate`
 - *Activate the virtual environment on Windows*
   - `.venv\Scripts\activate`
 - *Install dependencies*
   - `pip install -r requirements.txt`
 - *Call a specific script*
   - `python3 <script_name>.py`
 - *Deactivate virtual environment*
   - `deactivate`

# Testing

 - *Install pytest*
   - `pip3 install -U pytest`
 - *Run tests*
   - `pytest -rA`

# Topics
Here's what you can find here:

## [Algorithms](/algorithms/)
- [Binary search](/algorithms/binary_search_client.py) an efficent search within sorted lists
- [Binary Search Tree](/algorithms/binary_tree.py) a specially organized binary tree that allows divide and conquer searches
- [Inorder Tree Traversal](/algorithms/binary_search_tree_walker.py) Traverse a binary search tree inorder to list nodes in sorted ascending order
- [Merge sort](/algorithms/merge_sort_client.py) an efficient way to sort a list
- [Reverse Inorder Tree Traversal](/algorithms/binary_search_tree_walker.py) Traverse a binary search tree in reverse inorder to list nodes in sorted descending order

## [Azure](/azure/)
 - [Blob Storage](/azure/blob_storage/) ubiqutous file storage on Azure
   - [Create container](/azure/blob_storage/create_container.py) 
   - [List containers](/azure/blob_storage/list_containers.py) 
   - [Upload blob](/azure/blob_storage/upload_blob.py) 
   - [List blobs](/azure/blob_storage/list_blobs.py) 
   - [Download blob](/azure/blob_storage/download_blob.py)
 - [Key Vault](/azure/key_vault/) secret storage and crypto operations on Azure
   - [Set secret](/azure/key_vault/set_secret.py)
   - [Get secret](/azure/key_vault/get_secret.py)

## [Data Science](/data_science/)
 - [Load CSV into a pandas dataframe](/data_science/load_csv.py) 
 - [Group data and then find statistics for each group](/data_science/stats_by_group.py)

## [Interview Questions](/interview_questions/)
 - [Fizz Buzz](/interview_questions/fizz_buzz.py) A test that makes sure you can apply simple rules and cover all cases
 - [Reverse Linked List](/interview_questions/reverse_linked_list.py) Reason about interactions with a data structure and carefully manipulate how the data is organized
 - [Swap Numbers](/interview_questions/swap_numbers.py) Write a few cryptic calculations to placate an interviewer trying to trick you

## [Math](/math/)
 - [Multiply matrices](/math/multiply_matrices.py) Solve a system of linear equations using matrices

## [Standard Library](/standard_library/)
 - [Base64 encode and decode](/standard_library/base64_example.py) A way to represent binary information using plain text
 - [JSON encode and decode](/standard_library/json_example.py) A way to share data structures across languages and systems

# Support
 - How do I request a change?
   - Please submit an issue or a pull request
 - How fast will my request be added?
   - Probably not very fast for requests outside of a support package because this repo is maintained by a working professional
   - If you require fast, predictable responses, please purchase a support package
 - Can support package be purchased?
   - Yes, various support packages can be purchased and customized for your needs. Support areas available include:
   - On demand support videos
   - 1:1 and team coaching
   - New features and other modifications

## License

Licensed under

 - MIT license
   ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)