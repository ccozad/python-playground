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
 - *Change to specific add dir*
   - `cd <app>`
 - *Start the Flask app*
   - `flask run`
 - *Deactivate virtual environment*
   - `deactivate`

# Topics
 - [HTTP Methods](/web/flask/http_methods/app.py) A compact reference for using common HTTP methods such as GET, POST, PUT and DELETE