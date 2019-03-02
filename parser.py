import csv
from rdflib import OWL, Graph, Literal,  Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD , FOAF
import logging

logging.basicConfig()

input_file = csv.DictReader(open("allergy_v2.csv"))

output_graph = Graph()

LDT = Namespace("http://www.happyMeals.com/allergy#")
Product = URIRef(LDT["products"])
Nutrients = URIRef(LDT["nutrients"])
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
output_graph.bind('skos', skos)
output_graph.bind('owl', OWL)




for row in input_file:
    row = dict(row)

    # products csv
    # output_graph.add((Product, RDF.type, OWL.Class))
    # output_graph.add((Product, RDFS.subClassOf, OWL.Thing))
    # output_graph.add((Product+URIRef(row['NDB_Number']), OWL.product_id, Literal(row['NDB_Number'], lang='en')))
    # output_graph.add((Product+URIRef(row['NDB_Number']), OWL.product_name, Literal(row['long_name'], lang='en')))
    # output_graph.add((Product+URIRef(row['NDB_Number']), OWL.gtin_upc, Literal(row['gtin_upc'], lang='en')))
    # output_graph.add((Product+URIRef(row['NDB_Number']), OWL.store, Literal(row['manufacturer'], lang='en')))
    # output_graph.add((Product+URIRef(row['NDB_Number']), OWL.date_available, Literal(row['date_available'], lang='en')))
    # output_graph.add((Product+URIRef(row['NDB_Number']), OWL.ingredients, Literal(row['ingredients_english'], lang='en')))


    # nutrients csv
    # output_graph.add((URIRef(Nutrients+row['NDB_No']), OWL.product_id, Literal(row['NDB_No'], lang='en')))
    # output_graph.add((URIRef(Nutrients+row['NDB_No']), OWL.nutrient_id, Literal(row['Nutrient_Code'], lang='en')))
    # output_graph.add((URIRef(Nutrients+row['NDB_No']), OWL.nutrient_name, Literal(row['Nutrient_name'], lang='en')))
    # output_graph.add((URIRef(Nutrients+row['NDB_No']), OWL.derivation_Code, Literal(row['Derivation_Code'], lang='en')))
    # output_graph.add((URIRef(Nutrients+row['NDB_No']), OWL.nutrient_value, Literal(row['Output_value'], lang='en')))
    # output_graph.add((URIRef(Nutrients+row['NDB_No']), OWL.nutrient_uom, Literal(row['Output_uom'], lang='en')))

    #serving size csv
    # output_graph.add((URIRef(row['NDB_No']), FOAF.ndb_no, Literal(row['NDB_No'], lang='en')))
    # output_graph.add((URIRef(row['NDB_No']), FOAF.serving_size, Literal(row['Serving_Size'], lang='en')))
    # output_graph.add((URIRef(row['NDB_No']), FOAF.serving_size_uom, Literal(row['Serving_Size_UOM'], lang='en')))
    # output_graph.add((URIRef(row['NDB_No']), FOAF.household_serving_size, Literal(row['Household_Serving_Size'], lang='en')))
    # output_graph.add((URIRef(row['NDB_No']), FOAF.household_serving_size_uom, Literal(row['Household_Serving_Size_UOM'], lang='en')))
    # output_graph.add((URIRef(row['NDB_No']), FOAF.preparation_state, Literal(row['Preparation_State'], lang='en')))

    #food allergy
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.subject_id, Literal(row['SUBJECT_ID'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.birth_year, Literal(row['BIRTH_YEAR'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.gender_factor, Literal(row['GENDER_FACTOR'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.race_factor, Literal(row['RACE_FACTOR'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.ethenic_factor, Literal(row['ETHNICITY_FACTOR'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.AGE_START_YEARS, Literal(row['AGE_START_YEARS'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.AGE_END_YEARS, Literal(row['AGE_END_YEARS'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.SHELLFISH_ALG_START, Literal(row['SHELLFISH_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.SHELLFISH_ALG_END, Literal(row['SHELLFISH_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.FISH_ALG_START, Literal(row['FISH_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.FISH_ALG_END, Literal(row['FISH_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.MILK_ALG_START, Literal(row['MILK_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.MILK_ALG_END, Literal(row['MILK_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.SOY_ALG_START, Literal(row['SOY_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.SOY_ALG_END, Literal(row['SOY_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.EGG_ALG_START, Literal(row['EGG_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.EGG_ALG_END, Literal(row['EGG_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.WHEAT_ALG_START, Literal(row['WHEAT_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.WHEAT_ALG_END, Literal(row['WHEAT_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.PEANUT_ALG_START, Literal(row['PEANUT_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.PEANUT_ALG_END, Literal(row['PEANUT_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.SESAME_ALG_START, Literal(row['SESAME_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.SESAME_ALG_END, Literal(row['SESAME_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.TREENUT_ALG_START, Literal(row['TREENUT_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.TREENUT_ALG_END, Literal(row['TREENUT_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.WALNUT_ALG_START, Literal(row['WALNUT_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.WALNUT_ALG_END, Literal(row['WALNUT_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.PECAN_ALG_START, Literal(row['PECAN_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.PECAN_ALG_END, Literal(row['PECAN_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.PISTACH_ALG_START, Literal(row['PISTACH_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.PISTACH_ALG_END, Literal(row['PISTACH_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.ALMOND_ALG_START, Literal(row['ALMOND_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.ALMOND_ALG_END, Literal(row['ALMOND_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.BRAZIL_ALG_START, Literal(row['BRAZIL_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.BRAZIL_ALG_END, Literal(row['BRAZIL_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.HAZELNUT_ALG_START, Literal(row['HAZELNUT_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.HAZELNUT_ALG_END, Literal(row['HAZELNUT_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.CASHEW_ALG_START, Literal(row['CASHEW_ALG_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.CASHEW_ALG_END, Literal(row['CASHEW_ALG_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.ATOPIC_DERM_START, Literal(row['ATOPIC_DERM_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.ATOPIC_DERM_END, Literal(row['ATOPIC_DERM_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.allergic_rhinitis_start, Literal(row['ALLERGIC_RHINITIS_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.allergic_rhinitis_end, Literal(row['ALLERGIC_RHINITIS_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.asthma_start, Literal(row['ASTHMA_START'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.asthma_end, Literal(row['ASTHMA_END'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.first_asthmarx, Literal(row['FIRST_ASTHMARX'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.last_asthmarx, Literal(row['LAST_ASTHMARX'], lang='en')))
    output_graph.add((URIRef(row['SUBJECT_ID']), skos.num_asthmarx, Literal(row['NUM_ASTHMARX'], lang='en')))


output_graph.serialize(destination='allergy.rdf', format='xml')
output_graph.load("allergy.rdf")
