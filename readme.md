# The Trump presidency

After finishing reading Fire and Fury, the famous description of the Trump White House by Michael Wolff, I was left with an urgent desire to visualise at least some of the complex relationships that were being portrayed in this work. Not only would that be fun to do, it would also add to an understanding of the different forces and factions that make up the current administration.

From a computational point of view, it is only natural to envisage this force-field as a (directed) graph, so I decided to use the graph-database neo4j for this exercise. But because I did not want to type in all the Cypher queries in the neo4j web-engine, I used Python to read in some json and process that as a database-query.

Since Wolff's book describes three factions in the White House, apart from POTUS and his principal aids (which I dubbed 'Core'), I created three kinds of nodes: moderate repulicans (ModRep), republican establishment (RepEst), and altright. The first phase of the database-creationg reads in twentyone principal players divided among those four node-types. To make things easy, the relations between the principle representative of the faction (Kushner, Priebus, Bannon) and the persons aligned to this faction is always 'employs' (which leads to a rather disturbing relationship between e.g. Kusner and Ivanke Trump).

In the second phase, specific details between players in the White House force field are added to the graph. These relations have a specific name and direction, and feature the reference to the page number in Wolff's work where he describes this relationship.

I have used neo4jrestclient for the first phase and the more native neo4j.v1 for the second, for no apparant reason. Both the data and the scripts are available on github. In order to populate the database, the following commands must be executed:

<tt>
$ python create_data.py
$ pythin create_relations.py
<tt>

The following svg is the current result of this work. In it, in purple we see potus sitting in the middle with his closest advisors Hicks and Walsh above him. Surrounding him, we see the three main factions in yellow, blue and red. According to Wolff, the communication between Trump and the principal representative of these factions goes through his principal adviser Kellyann Conway, so there are edges from her node to the three main players. From these nodes, sevaral relations fan out and the force field kind of becomes apparant.

Now that I have this database ready, I will try to keep up with the (rapid) changes in the White House staff, using plain Cyper which will be collected in the update-script:

<tt>
$ python update.py
</tt>


Also, I will be adding functionality to the svg-graph (e.g. more information on the people involved) in the future.

B. Barnard
March 2018
