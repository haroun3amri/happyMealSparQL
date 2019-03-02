from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask
from flask_cors import CORS
from flask_jsonpify import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

CORS(app)


@app.route("/")
def hello():
    return jsonify({'text': 'Happy Meal App works!'})


class subscribersNurtirments(Resource):
    def get(self):
        sparql = SPARQLWrapper("http://localhost:8080/sparql")
        sparql.setQuery("""
       prefix h: <http://www.happyMeals.com/happyMeal.owl#>

   select *
 
 where {
  ?x   h:hasAlmondAllergy ?almond . ?x h:hasMilkAllergy  ?milk . ?x  h:hasPecanAllergy ?pecan . ?x h:hasFishAllergy ?fish . ?x h:hasPeanutAllergy ?peanut . ?x h:hasPistachioAllergy ?pistachio. ?x h:hasHazelAllergy ?hazel. ?x h:hasCashewAllergy ?cashew .?x  h:hasWheatAllergy ?wheat . ?x h:hasWalnutAllergy ?walnut. ?x h:hasSoyAllergy ?soy . ?x h:hasSeaFoodAllergy ?seafood . ?x h:hasSesameAllergy ?sesame . ?x h:hasEggAllergy ?egg .?x h:hasTreenutAllergy ?treenut .?x h:subject_id  ?id . ?x h:birth_year ?birth .?x foaf:gender ?gender. ?x h:ethnic_factor ?ethnic
filter (?id > "1" && ?birth>="1990" && ?gender="S0 - Male" && ?ethnic="E0 - Non-Hispanic" )
}
    """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results


class Subscribers(Resource):
    def get(self):
        sparql = SPARQLWrapper("http://localhost:8080/sparql")
        sparql.setQuery("""
         prefix h: <http://www.happyMeals.com/happyMeal.owl#>

select *
 
 where {
   ?x ?p ?p

}
      """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results


api.add_resource(subscribersNurtirments, '/subscribersNurtirments')  # route_1
api.add_resource(Subscribers, '/Subscribers')  # route_2

if __name__ == '__main__':
    app.run(port=5002)
