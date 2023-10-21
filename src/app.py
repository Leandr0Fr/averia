from flask import Flask
from routes.ping import ns_ping
from routes.predict import ns_predict
from flask_restx import Api
import os

api = Api()

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    #con esto se agrega los endpoints
    api.add_namespace(ns_ping)
    api.add_namespace(ns_predict)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug= False, port=os.getenv("PORT", default=8080))