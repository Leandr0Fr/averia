from flask_restx import Resource, Namespace, reqparse
from .response_generation import response_generation
from .connected_csv import *

ns_delete = Namespace("delete")

parser_fred = reqparse.RequestParser()
parser_fred.add_argument('id', type=int, help='id')
@ns_delete.route("/fred")
class Delete(Resource):
    @ns_delete.expect(parser_fred)
    def delete(self):
        args = parser_fred.parse_args()
        id = args['id']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id("csv/fred/fred.csv", id):
            return response_generation({"message": "ERROR! no exists ID"}, 404)
        
        delete_id(id, "csv/fred/fred.csv", "fred")
        return response_generation({"message": f"DELETE ID: {id}"}, 200)

parser_wini = reqparse.RequestParser()
parser_wini.add_argument('id', type=int, help='id')
@ns_delete.route("/wini")
class Delete(Resource):
    @ns_delete.expect(parser_wini)
    def delete(self):
        args = parser_wini.parse_args()
        id = args['id']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id("csv/wini/wini.csv", id):
            return response_generation({"message": "ERROR! no exists ID"}, 404)
        
        delete_id(id, "csv/wini/wini.csv", "wini")
        return response_generation({"message": f"DELETE ID: {id}"}, 200)

parser_lyso = reqparse.RequestParser()
parser_lyso.add_argument('id', type=int, help='id')
@ns_delete.route("/lyso")
class Delete(Resource):
    @ns_delete.expect(parser_lyso)
    def delete(self):
        args = parser_lyso.parse_args()
        id = args['id']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id("csv/lyso/lyso.csv", id):
            return response_generation({"message": "ERROR! no exists ID"}, 404)
        
        delete_id(id, "csv/lyso/lyso.csv", "wini")
        return response_generation({"message": f"DELETE ID: {id}"}, 200)
    
parser_all = reqparse.RequestParser()
parser_all.add_argument('model', type=str, help='name_model')
@ns_delete.route("/all")
class Delete(Resource):
    @ns_delete.expect(parser_all)
    def delete(self):
        args = parser_all.parse_args()
        name = args['model']
        is_str = isinstance(name, str)
        if not is_str:
            return response_generation({"message": "ERROR! name is not string"}, 400)
        if(name != "wini" and name != "fred" and name != "lyso"):
            return response_generation({"message": "ERROR! name model not exists"}, 404)
        delete_all(f"csv/{name}/{name}.csv")
        return response_generation({"message": f"DELETE ALL ROW: {name}"}, 200)    