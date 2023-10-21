from flask import Flask
from routes.hello import ns
from flask_restx import Api
import os

api = Api()

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    #con esto se agrega los endpoints
    api.add_namespace(ns)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug= False, port=os.getenv("PORT", default=8080))