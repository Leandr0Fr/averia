from flask_restx import Resource, Namespace, reqparse, inputs
from .response_generation import response_generation
from .connected_csv import *
from .routes import *
ns_retrieve = Namespace("retrieve")
# Define un analizador de solicitud para manejar la carga de archivos
parser_retrieve = reqparse.RequestParser()
parser_retrieve.add_argument('id_image', type=int, help='id_image')


@ns_retrieve.route("")
@ns_retrieve.doc(responses={200: "Retrieve ok!", 204: "ERROR! ID not exists", 400: "ERROR ID is not int"})
class Retrieve(Resource):
    @ns_retrieve.expect(parser_retrieve)
    def get(self):
        args = parser_retrieve.parse_args()
        id = args['id_image']

        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)

        data = {}
        if exists_id(CSV_FRED, id):
            data = get_info(id, CSV_FRED)
            data["model"] = "fred"
        elif exists_id(CSV_LYSO, id):
            data = get_info(id, CSV_LYSO)
            data["model"] = "lyso"
        elif exists_id(CSV_WINI, id):
            data = get_info(id, CSV_WINI)
            data["model"] = "wini"
        else:
            return response_generation({"message": "ERROR! ID not exists"}, 204)

        return response_generation(data, 200)
