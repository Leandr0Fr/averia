from flask_restx import Resource, Namespace, reqparse, inputs
from .response_generation import response_generation
from werkzeug.datastructures import FileStorage
from .model import prediction_tumor, prediction_pneumonia
ns_predict = Namespace("predict")
# Define un analizador de solicitud para manejar la carga de archivos
parser = reqparse.RequestParser()
parser.add_argument('image', type=FileStorage, location='files', required=True, help='Image file')
#ACORDARSE DEL inputs.boolean
parser.add_argument('debilidad_focal', type=inputs.boolean, help='debilidad_focal')
parser.add_argument('convulsiones', type=inputs.boolean, help='convulsiones')
parser.add_argument('perdida_visual', type=inputs.boolean, help='perdida_visual')

@ns_predict.route("/fred")
class Predict(Resource):
    @ns_predict.expect(parser)
    def post(self):
        args = parser.parse_args()
        debilidad = args['debilidad_focal']
        convulsiones = args['convulsiones']
        perdida_visual = args['perdida_visual']
        image = args['image']
    
        if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image.save("routes/image.png")
            response_data = {}
            class_probabilities = prediction_tumor()

            for tumor_type, probability in class_probabilities:
                response_data[tumor_type.lower()] = probability
            
            return response_generation(response_data, 200)
        else:
            return response_generation({"message" : "I'm a teapot!"}, 418)
        
parser_wini = reqparse.RequestParser()
parser_wini.add_argument('image', type=FileStorage, location='files', required=True, help='Image file')
@ns_predict.route("/wini")
class Predict(Resource):
    @ns_predict.expect(parser_wini)
    def post(self):
        args = parser_wini.parse_args()
        image = args['image']
        if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image.save("routes/image.png")
            response_data = {}
            class_probabilities = prediction_pneumonia()

            for tumor_type, probability in class_probabilities:
                response_data[tumor_type.lower()] = probability
            
            return response_generation(response_data, 200)
        else:
            return response_generation({"message" : "I'm a teapot!"}, 418)