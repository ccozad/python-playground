![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ccozad/python-playground)
![GitHub top language](https://img.shields.io/github/languages/top/ccozad/python-playground)
![GitHub](https://img.shields.io/github/license/ccozad/python-playground)

# Overview
 A collection of random Python solutions. If anything helps you here please give this repo a star.

# General Setup
It's recommended that you use a virtual environment to run each group of scripts. Each folder has its own requirements.txt file. the process for setting up your environment look like

*Move to the topic folder*

`cd <topic_folder>`

*Create a virtual environment*

`python3 -m venv .venv`

*Activate the virtual environment on Mac*

`source .venv/bin/activate`

*Activate the virtual environment on Windows*

`.venv\Scripts\activate`

*Install dependencies*

`pip install -r requirements.txt`

*Call a specific script*

`python3 <script_name>.py`

*Deactivate virtual environment*

`deactivate`

# Testing

*Install pytest*

`pip3 install -U pytest`

*Run tests*

`pytest -rA`

# Topics
Here's what you can find here:

## Algorithms
- Binary search, an efficent search for sorted lists
   - `pytest` to run tests in`test_binary_search_client.py`

## Azure
 - Blob Storage (Ubiqutous file storage on Azure)
   - Create container `python3 create_container.py`
   - List containers `python3 list_containers.py`
   - Upload blob `python3 upload_blob.py`
   - List blobs `python3 list_blobs.py`
   - Download blob `python3 download_blob.py`

## Data Science
- Group data and then find statistics for each group 
   - `python3 stats_by_group.py`
- Load CSV into a pandas dataframe 
   - `python3 load_csv.py`