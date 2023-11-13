from flask import Flask
from routes.ping import ns_ping
from routes.predict import ns_predict
from routes.feedback import ns_feedback
from routes.download import ns_download
from routes.delete import ns_delete
from routes.retrieve import ns_retrieve
from flask_restx import Api
import os

api = Api()

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    # con esto se agrega los endpoints
    api.add_namespace(ns_ping)
    api.add_namespace(ns_predict)
    api.add_namespace(ns_feedback)
    api.add_namespace(ns_download)
    api.add_namespace(ns_delete)
    api.add_namespace(ns_retrieve)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=8080))
