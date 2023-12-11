from flask_restx import Resource, Namespace, reqparse, inputs
from app.utils.response_generation import response_generation
from werkzeug.datastructures import FileStorage
from .model import prediction_tumor, prediction_pneumonia, prediction_kidney
from app.utils.connected_csv import *
from app.utils.routes import *

ns_predict = Namespace("predict")

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
@ns_predict.doc(responses={200: "Prediction ok!", 400: "¡ERROR! ID is not int / ¡ERROR! existing ID ", 404: "¡ERROR! image not found", 418: "I'm a teapot!"})
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
            name = str(id)

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
@ns_predict.doc(responses={200: "Prediction ok!", 400: "¡ERROR! ID is not int / ¡ERROR! existing ID ", 404: "¡ERROR! image not found", 418: "¡I'm a teapot! (No se le paso un archivo con la extensión correcta)"})
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
            name = str(id)

            image.save(f"{IMAGES_WINI}/{name}.png")
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
    'hermaturia', type=inputs.boolean, help='hermaturia')

parser_lyso .add_argument(
    'dolor_lumbar', type=inputs.boolean, help='dolor_lumbar')

parser_lyso .add_argument(
    'dolor_abdominal', type=inputs.boolean, help='dolor_abdominal')

parser_lyso .add_argument(
    'fiebre', type=inputs.boolean, help='fiebre')

parser_lyso .add_argument(
    'perdida_peso', type=inputs.boolean, help='perdida_peso')

@ns_predict.route("/lyso")
@ns_predict.doc(responses={200: "Prediction ok!", 400: "ERROR! ID is not int / ERROR existing ID ", 404: "ERROR! image not found", 418: "I'm a teapot! (No se le paso un archivo con la extensión correcta)"})
class Predict(Resource):
    @ns_predict.expect(parser_lyso)
    def post(self):
        args = parser_lyso.parse_args()
        hermaturia = 1 if args['hermaturia'] else 0
        dolor_lumbar = 1 if args['dolor_lumbar'] else 0
        dolor_abdominal = 1 if args['dolor_abdominal'] else 0
        fiebre = 1 if args['fiebre'] else 0
        perdida_peso = 1 if args['perdida_peso'] else 0

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
            name = str(id)

            image.save(f"{IMAGES_LYSO}/{name}.png")
            response_data = {}
            class_probabilities = prediction_kidney(name)

            for class_type, probability in class_probabilities:
                response_data[class_type.lower()] = probability

            append_predict_lyso(id, f"images/{name}.png", hermaturia,
                                dolor_lumbar, dolor_abdominal, fiebre, perdida_peso)
            return response_generation(response_data, 200)
        else:
            return response_generation({"message": "I'm a teapot!"}, 418)