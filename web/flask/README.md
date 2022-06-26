# Introduction
Flask is a light weight framework that aimes to keep the core simple but extensible. Most decisions such as database technology, validation and advanced upload format are left to the developer and solved through a catalog of plugins.

# Setup
 - *Move to the topic folder*
   - `cd web/flask`
 - *Create a virtual environment*
   - `python3 -m venv .venv`
 - *Activate the virtual environment on Mac*
   - `source .venv/bin/activate`
 - *Activate the virtual environment on Windows*
   - `.venv\Scripts\activate`
 - *Install dependencies*
   - `pip install -r requirements.txt`
 - *Change to specific app dir*
   - `cd <app>`
 - *Start the Flask app*
   - `flask run`
 - *Deactivate virtual environment*
   - `deactivate`

# Topics
 - [File uploads](/web/flask/file_uploads/app.py) A reference for uploading a file and saving it to a random name
 - [HTTP methods](/web/flask/http_methods/app.py) A compact reference for using common HTTP methods such as GET, POST, PATCH and DELETE
    - [HTTP methods video tutorial](https://www.youtube.com/watch?v=8pZwHItj0tg)
 - [SQL database](/web/flask/sql_database/) CRUD operations with a database over a REST API