from flask_restx import Resource, Namespace
from .response_generation import response_generation
ns = Namespace("predict")

@ns.route("")
class Predict(Resource):
    def post(self):
        return response_generation({"message" : "Endpoint conectado"}, 200)
