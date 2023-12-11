from flask_restx import Resource, Namespace
from app.utils.response_generation import response_generation
ns_ping = Namespace("ping")

@ns_ping.route("")
@ns_ping.doc(responses={200: "API on!"})
class Ping(Resource):
    def get(self):
        return response_generation({"message": "API on!"}, 200)
