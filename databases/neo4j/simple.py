# This example assumes you have the movie database loadeed
from neo4j import GraphDatabase

import os
import dotenv
dotenv.load_dotenv()
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")
auth = (neo4j_user, neo4j_password)

with GraphDatabase.driver(neo4j_uri, auth=auth) as driver:
    driver.verify_connectivity()

    print("Successfully connected to Neo4j")

    print("Running a simple query:")

    records, summary, keys = driver.execute_query(
        "MATCH (actor:Person {name: $name})-[:ACTED_IN]->(movies) RETURN actor,movies",
        name="Tom Hanks",
        database_="neo4j",
    )

    print("Movies that Tom Hanks acted in:")

    # Loop through results and do something with them
    for movie in records:
        title = movie.data().get("movies").get("title")
        print(" - ", title)

    # Summary information
    print("\nThe query `{query}` returned {records_count} records in {time} ms.".format(
        query=summary.query, records_count=len(records),
        time=summary.result_available_after,
    ))

