from flask_restx import Resource, Namespace
from .response_generation import response_generation
import subprocess
ns_ping = Namespace("ping")

@ns_ping.route("")
class Ping(Resource):
    def get(self):
        result = subprocess.run(["ls -la"], stdout=subprocess.PIPE, text=True)
# Imprimir la salida del comando
        print("Directorio actual pinga:", result.stdout)
        return response_generation({"message" : "API on!"}, 200)
