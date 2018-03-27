from neo4j.v1 import GraphDatabase, Relationship
import json

data = json.load(open("data/relations.json"))
rels = data['relations']

uri="bolt://localhost:7687/"
driver = GraphDatabase.driver(uri)
s = driver.session()

for r in rels:
    stmt = "MATCH (p1) where p1.name='{0}' MATCH (p2) where p2.name='{1}' CREATE (p1)-[:{2}{3}]->(p2)"
    print (stmt.format(r['p1'], r['p2'], r['r'], "{p:"+r['page']+"}"))
    s.run(stmt.format(r['p1'], r['p2'], r['r'], "{p:"+r['page']+"}"))

'''
stmt = "MATCH (p1) where p1.name='{0}' MATCH (p2) where p2.name='{1}' CREATE (p1)-[:{2}]->(p2)"
s.run(stmt.format("Donald Trump", "Katie Walsh", "Hates"))
MATCH (p1) where p1.name='Kellyann Conway' MATCH (p2) where p2.name='Reince Priebus' CREATE (p1)-[:connection_to{p:81}]->(p2)"
'''
