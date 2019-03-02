import rdflib

g = rdflib.Graph()

g.parse("products.rdf")

qres = g.query(
    """SELECT DISTINCT ?a ?b
       WHERE {
          ?a foaf:knows ?b .
          ?a foaf:product_name ?a .
          ?b foaf:ingredient_name ?b .
       }""")

for row in qres:
    print("%s knows %s" % row)