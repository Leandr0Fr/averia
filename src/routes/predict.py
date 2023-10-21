from flask_restx import Resource, Namespace, reqparse, inputs
from .response_generation import response_generation
from werkzeug.datastructures import FileStorage

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
            image.save("image.png")
            return response_generation({"message" : "todo piola"}, 200)
        else:
            return response_generation({"message" : "I'm a teapot!"}, 418)