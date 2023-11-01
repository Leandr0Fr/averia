from flask_restx import Resource, Namespace, reqparse, inputs
from .response_generation import response_generation
from werkzeug.datastructures import FileStorage
from .model import prediction_tumor, prediction_pneumonia, prediction_kidney
from .connected_csv import *
import time
from .routes import *

ns_predict = Namespace("predict")
# Define un analizador de solicitud para manejar la carga de archivos
parser_fred = reqparse.RequestParser()
parser_fred.add_argument('image', type=FileStorage,
                         location='files', help='Image file')
parser_fred.add_argument('id_image', type=int, help='Id_image')
parser_fred.add_argument(
    'debilidad_focal', type=inputs.boolean, help='debilidad_focal')
parser_fred.add_argument(
    'convulsiones', type=inputs.boolean, help='convulsiones')
parser_fred.add_argument(
    'perdida_visual', type=inputs.boolean, help='perdida_visual')

@ns_predict.route("/fred")
class Predict(Resource):
    @ns_predict.expect(parser_fred)
    def post(self):
        args = parser_fred.parse_args()
        debilidad = 1 if args['debilidad_focal'] else 0
        convulsiones = 1 if args['convulsiones'] else 0
        perdida_visual = 1 if args['perdida_visual'] else 0
        image = args['image']
        id = args['id_image']

        if image == None:
            return response_generation({"message": "ERROR! image not found"}, 404)
        if exists_id(CSV_FRED, id):
            return response_generation({"message": "ERROR! existing ID"}, 400)
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = get_millsec()

            image.save(f"{IMAGES_FRED}/{name}.png")
            response_data = {}
            class_probabilities = prediction_tumor(name)

            for tumor_type, probability in class_probabilities:
                response_data[tumor_type.lower()] = probability

            append_predict_fred(id, f"images/{name}.png", debilidad,
                                convulsiones, perdida_visual)
            return response_generation(response_data, 200)
        else:
            return response_generation({"message": "I'm a teapot!"}, 418)


parser_wini = reqparse.RequestParser()
parser_wini.add_argument('image', type=FileStorage,
                         location='files', help='Image file')
parser_wini.add_argument('id_image', type=int, help='Id_image')
parser_wini.add_argument(
    'puntada_lateral', type=inputs.boolean, help='puntada_lateral')
parser_wini.add_argument('fiebre', type=inputs.boolean, help='fiebre')
parser_wini.add_argument('dificultad_respiratoria',
                         type=inputs.boolean, help='dificultad_respiratoria')


@ns_predict.route("/wini")
class Predict(Resource):
    @ns_predict.expect(parser_wini)
    def post(self):
        args = parser_wini.parse_args()
        image = args['image']
        id = args['id_image']
        puntada_lateral = 1 if args['puntada_lateral'] else 0
        fiebre = 1 if args['fiebre'] else 0
        dificultad_respiratoria = 1 if args['dificultad_respiratoria'] else 0
        
        if image == None:
            return response_generation({"message": "ERROR! image not found"}, 404)
        if exists_id(CSV_WINI, id):
            return response_generation({"message": "ERROR! existing ID"}, 400)
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = get_millsec()

            image.save(f"{IMAGES_FRED}/{name}.png")
            response_data = {}
            class_probabilities = prediction_pneumonia(name)

            for type, probability in class_probabilities:
                response_data[type.lower()] = probability

            append_predict_wini(id, f"images/{name}.png", puntada_lateral,
                                fiebre, dificultad_respiratoria)
            return response_generation(response_data, 200)
        else:
            return response_generation({"message": "I'm a teapot!"}, 418)


parser_lyso = reqparse.RequestParser()
parser_lyso .add_argument('image', type=FileStorage,
                         location='files', help='Image file')
parser_lyso .add_argument('id_image', type=int, help='Id_image')
parser_lyso .add_argument(
    'placeholder1', type=inputs.boolean, help='placeholder1')
parser_lyso .add_argument(
    'placeholder2', type=inputs.boolean, help='placeholder2')
parser_lyso .add_argument(
    'placeholder3', type=inputs.boolean, help='placeholder3')

@ns_predict.route("/lyso")
class Predict(Resource):
    @ns_predict.expect(parser_lyso)
    def post(self):
        args = parser_lyso.parse_args()
        placeholder1 = 1 if args['placeholder1'] else 0
        placeholder2 = 1 if args['placeholder2'] else 0
        placeholder3 = 1 if args['placeholder3'] else 0
        image = args['image']
        id = args['id_image']

        if image == None:
            return response_generation({"message": "ERROR! image not found"}, 404)
        if exists_id(CSV_LYSO, id):
            return response_generation({"message": "ERROR! existing ID"}, 400)
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = get_millsec()

            image.save(f"{IMAGES_LYSO}/{name}.png")
            response_data = {}
            class_probabilities = prediction_kidney(name) 

            for class_type, probability in class_probabilities:
                response_data[class_type.lower()] = probability

            append_predict_lyso(id, f"images/{name}.png", placeholder1,
                                placeholder2, placeholder3)
            return response_generation(response_data, 200)
        else:
            return response_generation({"message": "I'm a teapot!"}, 418)

def get_millsec():
    return str(int(round(time.time() * 1000)))