from flask_restx import Resource, Namespace, reqparse, inputs
from .response_generation import response_generation
from .utils import *

ns_feedback = Namespace("feedback")
# Define un analizador de solicitud para manejar la carga de archivos
parser_fred = reqparse.RequestParser()
parser_fred.add_argument('id_image', type= int, help='id_image')
parser_fred.add_argument('glioma', type=inputs.boolean, help='glioma')
parser_fred.add_argument('meningioma', type=inputs.boolean, help='meningioma')
parser_fred.add_argument('pituitary', type=inputs.boolean, help='pituitary')
parser_fred.add_argument('no_tumor', type=inputs.boolean, help='no_tumor')

@ns_feedback.route("/fred")
class Feedback(Resource):
    @ns_feedback.expect(parser_fred)
    def post(self):
        args = parser_fred.parse_args()
        id = args['id_image']
        glioma = args['glioma']
        meningioma = args['meningioma']
        pituitary = args['pituitary']
        no_tumor = args['no_tumor']
        is_int = type(id)

        true_count = sum([glioma, meningioma, pituitary, no_tumor])
        if true_count > 1:
            return response_generation({"message": "ERROR! there is more than one true value"}, 418)
        if glioma == False and meningioma == False and pituitary == False and no_tumor == False:
            return response_generation({"message": "ERROR! all values is false"}, 418)
        if (glioma == None or id == None or meningioma == None or pituitary == None or no_tumor == None or is_int != int):
            return response_generation({"message" : "ERROR! Values Null"}, 418)
        return response_generation({"message" : "POST ACCEPTED"}, 200)

parser_wini = reqparse.RequestParser()

parser_wini.add_argument('id_image', type=int, help='Id_image')
parser_wini.add_argument('pneumonia', type=inputs.boolean, help='pneumonia')
parser_wini.add_argument('no_pneumonia', type=inputs.boolean, help='no_pneumonia')

@ns_feedback.route("/wini")
class Predict(Resource):
    @ns_feedback.expect(parser_wini)
    def post(self):
        args = parser_wini.parse_args()
        id = args['id_image']
        if not exists_id ("csv/wini.csv", id):
            return response_generation({"message": "ERROR! no exists ID"}, 418)
        
        pneumonia = 1 if args['pneumonia'] else 0
        no_pneumonia = 1 if args['no_pneumonia'] else 0
        
        if (pneumonia + no_pneumonia) == 2:
            return response_generation({"message": "ERROR! there is more than one true value"}, 418)
        if (pneumonia + no_pneumonia) == 0:
            return response_generation({"message": "ERROR! all values is false"}, 418)
    
        append_feedback_wini(id, pneumonia, no_pneumonia)
        return response_generation({"message" : "POST ACCEPTED"}, 200)