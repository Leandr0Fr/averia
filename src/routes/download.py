from flask_restx import Resource, Namespace
from .response_generation import response_generation
from .connected_csv import *
from flask import send_file
import shutil
import os
from .routes import *

ns_download = Namespace("download")

@ns_download.route("/fred")
class Download(Resource):
    def get(self):
        to_zip(FOLDER_FRED, "fred")
        file = DOWNLOAD_FRED_ROUTE
        return send_file(file, as_attachment=True, download_name="fred.zip")

@ns_download.route("/wini")
class Download(Resource):
    def get(self):
        to_zip(FOLDER_WINI, "wini")
        file = DOWNLOAD_WINI_ROUTE
        return send_file(file, as_attachment=True, download_name="wini.zip")

@ns_download.route("/lyso")
class Download(Resource):
    def get(self):
        to_zip(FOLDER_LYSO, "lyso")
        file = DOWNLOAD_LYSO_ROUTE
        return send_file(file, as_attachment=True, download_name="lyso.zip")

def to_zip(route, name):
    folder = route
    name_zip = name
    route_save = "download/"
    shutil.make_archive(os.path.join(route_save, name_zip), 'zip', folder)