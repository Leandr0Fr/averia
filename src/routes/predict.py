from flask_restx import Resource, Namespace, reqparse
from .response_generation import response_generation
from werkzeug.datastructures import FileStorage

ns_predict = Namespace("predict")
# Define un analizador de solicitud para manejar la carga de archivos
parser = reqparse.RequestParser()
parser.add_argument('image', type=FileStorage, location='files', required=True, help='Image file')
@ns_predict.route("")
class Predict(Resource):
    @ns_predict.expect(parser)
    def post(self):
        args = parser.parse_args()
        image = args['image']
        if image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image.save("image.png")
            return response_generation({"message" : "todo piola"}, 200)
        else:
            return response_generation({"message" : "I'm a teapot!"}, 418)