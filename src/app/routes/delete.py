from flask_restx import Resource, Namespace, reqparse
from app.utils.response_generation import response_generation
from app.utils.connected_csv import *
from app.utils.routes import *
ns_delete = Namespace("delete")

parser_fred = reqparse.RequestParser()
parser_fred.add_argument('id', type=int, help='id')


@ns_delete.route("/fred")
@ns_delete.doc(responses={200: "ID DELETED", 204: "ERROR! ID not exists", 400: "ERROR! ID is not int"})
class Delete(Resource):
    @ns_delete.expect(parser_fred)
    def delete(self):
        args = parser_fred.parse_args()
        id = args['id']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id(CSV_FRED, id):
            return response_generation({"message": "ERROR! ID not exists"}, 204)

        delete_id(id, CSV_FRED, "fred")
        return response_generation({"message": f"ID DELETED: {id}"}, 200)


parser_wini = reqparse.RequestParser()
parser_wini.add_argument('id', type=int, help='id')


@ns_delete.route("/wini")
@ns_delete.doc(responses={200: "ID DELETED", 204: "ERROR! ID not exists", 400: "ERROR! ID is not int"})
class Delete(Resource):
    @ns_delete.expect(parser_wini)
    def delete(self):
        args = parser_wini.parse_args()
        id = args['id']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id(CSV_WINI, id):
            return response_generation({"message": "ERROR! ID not exists"}, 204)

        delete_id(id, CSV_WINI, "wini")
        return response_generation({"message": f"ID DELETED: {id}"}, 200)


parser_lyso = reqparse.RequestParser()
parser_lyso.add_argument('id', type=int, help='id')


@ns_delete.route("/lyso")
@ns_delete.doc(responses={200: "ID DELETED", 204: "ERROR! ID not exists", 400: "ERROR! ID is not int"})
class Delete(Resource):
    @ns_delete.expect(parser_lyso)
    def delete(self):
        args = parser_lyso.parse_args()
        id = args['id']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id(CSV_LYSO, id):
            return response_generation({"message": "ERROR! ID not exists"}, 204)

        delete_id(id, CSV_LYSO, "lyso")
        return response_generation({"message": f"ID DELETED: {id}"}, 200)


parser_all = reqparse.RequestParser()
parser_all.add_argument('model', type=str, help='name_model')


@ns_delete.route("/all")
@ns_delete.doc(responses={200: "DELETED ALL ROWS", 204: "ERROR! model name not exists", 400: "ERROR! name is not string"})
class Delete(Resource):
    @ns_delete.expect(parser_all)
    def delete(self):
        args = parser_all.parse_args()
        name = args['model']
        is_str = isinstance(name, str)
        if not is_str:
            return response_generation({"message": "ERROR! name is not string"}, 400)
        if (name != "wini" and name != "fred" and name != "lyso"):
            return response_generation({"message": "ERROR! model name not exists"}, 204)
        delete_all(f"{CSV_ROUTE}/{name}/{name}.csv", name)
        return response_generation({"message": f"DELETE ALL ROWS: {name}"}, 200)