from flask_restx import Resource, Namespace
from .response_generation import response_generation
from .connected_csv import *
from flask import send_file
import shutil
import os

ns_download = Namespace("download")

@ns_download.route("/fred")
class Download(Resource):
    def get(self):
        to_zip("csv/fred", "fred")
        file = "download/fred.zip"
        return send_file(file, as_attachment=True, download_name="fred.zip")

@ns_download.route("/wini")
class Download(Resource):
    def get(self):
        to_zip("csv/wini", "wini")
        file = "download/wini.zip"
        return send_file(file, as_attachment=True, download_name="wini.zip")

@ns_download.route("/x")
class Download(Resource):
    def get(self):
        archivo = "images/placeholder.txt"
        return send_file(archivo, as_attachment=True, download_name="placeholder.txt")

def to_zip(route, name):
    folder = route
    name_zip = name
    route_save = "download/"
    shutil.make_archive(os.path.join(route_save, name_zip), 'zip', folder)