from neo4jrestclient.client import GraphDatabase
import json
import time

start = time.time()
data = json.load(open("data/persons.json"))
uri="http://localhost:7474"
db=GraphDatabase(uri)

print ("Deleting all previous records.")
db.query("MATCH () -[r]-() DELETE r")
db.query('MATCH (r) DELETE r')

print ("Inserting data.")
for key in data:
    print ("Creating nodes for {}".format(key))
    ctr = 0
    main_node = None

    k = db.labels.create(key)
    persons = data[key]
    for person in persons:
        node = db.nodes.create(name=person['name'], role=person['role'])
        if (ctr==0): main_node = node
        else: main_node.relationships.create("employs", node)
        k.add(node)
        ctr += 1

    print ("{} nodes added.".format(ctr))

exec = round(time.time() - start, 2)
print ("Creation took {} secs".format(exec))
print ("Done.")
