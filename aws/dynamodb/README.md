# Install Dependencies

1. Change into the /aws/dynamodb
2. Create a virtual environment
3. `pip install -r requirements.txt`

# Execution Order

The recomended order to run things in this area is

 1. `create_tables.py`
 2. `list_tables.py`
 3. `put_items.py`
 4. `scan_items.py`

 # Key Terms

  - **Attribute** A fundamental data element, a detail of an item record
  - **Item** A group of attributes that makes up one record in a table
  - **Global Secondary Index** A partition and sort key index that can be different than the primary key
  - **Local Secondary Index** An index that uses the same primary key but a different sort key
  - **Primary Key** A unique identifier for each item in a table
  - **Table** A collection of items retrieved by key

**[Back to start](https://github.com/ccozad/python-playground)**