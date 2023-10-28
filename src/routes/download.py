from flask_restx import Resource, Namespace
from .response_generation import response_generation
from .connected_csv import *
from flask import send_file
ns_download = Namespace("download")

@ns_download.route("/fred")
class Download(Resource):
    def get(self):
        archivo = "images/placeholder.txt"
        return send_file(archivo, as_attachment=True, download_name="placeholder.txt")

@ns_download.route("/wini")
class Download(Resource):
    def get(self):
        archivo = "images/placeholder.txt"
        return send_file(archivo, as_attachment=True, download_name="placeholder.txt")

@ns_download.route("/x")
class Download(Resource):
    def get(self):
        archivo = "images/placeholder.txt"
        return send_file(archivo, as_attachment=True, download_name="placeholder.txt")
