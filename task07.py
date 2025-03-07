# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yPniC8cCIRK0ofpUQK_h0bcNOa4CroCF

**Task 07: Querying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, FOAF

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage + "/rdf/example6.rdf", format="xml")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://somewhere#")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
q1 = """
        SELECT ?subclass
        WHERE { 
            ?subclass rdfs:subClassOf ns:LivingThing .
        }
"""
# Visualize the results

for r in g.query(q1):
    print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = """
     SELECT ?instances
     WHERE {
         ?instances rdf:type ns:Person.
     }
"""
# Visualize the results
for r in g.query(q2):
    print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**"""

# TO DO
q3 = """
     SELECT ?individuals
     WHERE {
         {?individuals rdf:type ns:Person}
         UNION
         {?individuals rdf:type ns:Animal}
     }
"""
# Visualize the results
for r in g.query(q3):
    print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""
from rdflib.plugins.sparql import prepareQuery

# TO DO
q4 = prepareQuery("""
    SELECT ?person
    WHERE {
       ?person foaf:knows ns:RockySmith .
       ?person rdf:type ns:Person .
    }
""", initNs={"rdf":RDF, "foaf":FOAF, "ns":Namespace("http://somewhere#")})

# Visualize the results
for r in g.query(q4):
    print(r.person)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
q5 = prepareQuery("""
    SELECT ?animal
    WHERE {
        ?animal foaf:knows ?otherAnimal .
        ?animal rdf:type ns:Animal .
        ?otherAnimal rdf:type ns:Animal .
    }
""", initNs={"rdf":RDF, "foaf":FOAF, "ns":Namespace("http://somewhere#")})

# Visualize the results
for r in g.query(q5):
    print(r)
"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
q6 = prepareQuery("""
    SELECT  ?individual ?age
    WHERE {
        ?individual rdf:type ?class .
        ?class rdfs:subClassOf* ns:LivingThing .
        ?individual foaf:age ?age .
    }
""", initNs={"rdf":RDF, "rdfs": RDFS, "foaf": FOAF, "ns":Namespace("http://somewhere#")})
# Visualize the results
for r in g.query(q6):
   print(r)
