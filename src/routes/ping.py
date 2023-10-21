from flask_restx import Resource, Namespace
from response_generation import response_generation
ns = Namespace("ping")

@ns.route("")
class Ping(Resource):
    def get(self):
        return response_generation({"message" : "API on!"}, 200)
