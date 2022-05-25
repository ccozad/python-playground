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
 - *Initialize database*
   - `python`
   - `from app import db`
   - `db.create_all()`
 - *Start the Flask app*
   - `flask run`
 - *Deactivate virtual environment*
   - `deactivate`

# Examples

## Create a Level

```
curl --location --request POST 'http://127.0.0.1:5000/levels/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "The Green Field"
}'
```

## Get All Levels

```
curl --location --request GET 'http://127.0.0.1:5000/levels/'
```