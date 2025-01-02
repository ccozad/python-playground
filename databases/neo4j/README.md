# Introduction

This set of examples assumes you have the movie database loaded

See https://neo4j.com/graphgists/cypher-introduction-social-movie-database/ for details on the movie database.

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Python virtual environment
 - Environment variables

## Python Virtual Environment

 - Move to the neo4j folder
   - `cd <neo4j>`
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

## Environment Variables

Create a file named `.env` with the contents shown below

```
NEO4J_URI=<address>
NEO4J_USER=<user>
NEO4J_PASSWORD=<password>
```

# Example Output

## simple.py

```text
python3 simple.py

Successfully connected to Neo4j
Running a simple query:
Movies that Tom Hanks acted in:
 -  Apollo 13
 -  You've Got Mail
 -  A League of Their Own
 -  Joe Versus the Volcano
 -  That Thing You Do
 -  The Da Vinci Code
 -  Cloud Atlas
 -  Cast Away
 -  The Green Mile
 -  Sleepless in Seattle
 -  The Polar Express
 -  Charlie Wilson's War

The query `MATCH (actor:Person {name: $name})-[:ACTED_IN]->(movies) RETURN actor,movies` returned 12 records in 9 ms.
```