from neo4j.v1 import GraphDatabase, Relationship
import json

data = json.load(open("data/relations.json"))
rels = data['relations']

uri="bolt://localhost:7687/"
driver = GraphDatabase.driver(uri)
s = driver.session()

with s.begin_transaction() as tx:
    query = """MATCH (flyn) WHERE flyn.name="Michael Flynn"
            CREATE (mcmas:ModRep { name:"Herbert McMaster", role:"NSA from Feb 2017"} ),
            (flyn)-[:replaced_by {p:188}]->(mcmas)"""
    tx.run(query)
    tx.commit()
