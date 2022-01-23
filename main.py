from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

personal = {}

class resources(Resource):
    def get(self):
        # response = {"msg" : "Welcome to my Codings"}
        return personal

    def post(self):
        name = request.form["name"]
        live = request.form["live"]
        address = request.form["address"]
        personal["name"] = name
        personal["live"] = live
        personal["address"] = address
        response = {"msg" : "Data has been validate"}
        return response

api.add_resource(resources, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
  app.run(debug=True)