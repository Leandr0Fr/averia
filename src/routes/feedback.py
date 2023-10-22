from flask_restx import Resource, Namespace, reqparse, inputs
from .response_generation import response_generation
ns_fb = Namespace("feedback")
# Define un analizador de solicitud para manejar la carga de archivos
parser_fred = reqparse.RequestParser()

parser_fred.add_argument('id_image', type=inputs.int_range, required=True, help='Id_image')
parser_fred.add_argument('glioma', type=inputs.boolean, required=True, help='glioma')
parser_fred.add_argument('meningioma', type=inputs.boolean, required=True, help='meningioma')
parser_fred.add_argument('pituitary', type=inputs.boolean, required=True, help='pituitary')
parser_fred.add_argument('no_tumor', type=inputs.boolean, required=True, help='no_tumor')

@ns_fb.route("/fred")
class Predict(Resource):
    @ns_fb.expect(parser_fred)
    def post(self):
        args = parser_fred.parse_args()
        id = args['id_image']
        glioma = args['glioma']
        meningioma = args['meningioma']
        pituitary = args['pituitary']
        no_tumor = args['no_tumor']
        if (glioma == None or id == None or meningioma == None or pituitary == None or no_tumor == None):
            return response_generation({"message" : "ERROR! Values Null"}, 418)
        return response_generation({"message" : "POST ACCEPTED"}, 200)
        
parser_wini = reqparse.RequestParser()

parser_wini.add_argument('id_image', type=inputs.int_range, required=True, help='Id_image')
parser_wini.add_argument('pneumonia', type=inputs.boolean, required=True, help='pneumonia')
parser_wini.add_argument('no_pneumonia', type=inputs.boolean, required=True, help='no_pneumonia')

@ns_fb.route("/wini")
class Predict(Resource):
    @ns_fb.expect(parser_wini)
    def post(self):
        args = parser_fred.parse_args()
        id = args['id_image']
        pneumonia = args['pneumonia']
        no_pneumonia = args['no_pneumonia']
        if (pneumonia == None or id == None or no_pneumonia == None):
            return response_generation({"message" : "ERROR! Values Null"}, 418)
        return response_generation({"message" : "POST ACCEPTED"}, 200)