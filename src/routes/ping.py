from flask_restx import Resource, Namespace
from .response_generation import response_generation
import subprocess
ns_ping = Namespace("ping")

@ns_ping.route("")
class Ping(Resource):
    def get(self):
        comando = "ls -la"

# Utiliza subprocess para ejecutar el comando   
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Verifica si la ejecución fue exitosa
        if resultado.returncode == 0:
            # Imprime la salida del comando
            print("Salida del comando:")
            print(resultado.stdout)
        else:
            # Imprime mensajes de error en caso de que ocurra un error
            print("Error al ejecutar el comando:")
            print(resultado.stderr)
        return response_generation({"message" : "API on!"}, 200)
