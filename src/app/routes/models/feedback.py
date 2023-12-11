from flask_restx import Resource, Namespace, reqparse, inputs
from app.utils.response_generation import response_generation
from app.utils.connected_csv import *
from app.utils.routes import *

ns_feedback = Namespace("feedback")

parser_fred = reqparse.RequestParser()
parser_fred.add_argument('id_image', type=int, help='id_image')
parser_fred.add_argument('glioma', type=inputs.boolean, help='glioma')
parser_fred.add_argument('meningioma', type=inputs.boolean, help='meningioma')
parser_fred.add_argument('pituitary', type=inputs.boolean, help='pituitary')
parser_fred.add_argument('no_tumor', type=inputs.boolean, help='no_tumor')
parser_fred.add_argument('comment', type=str, help='comment')


@ns_feedback.route("/fred")
@ns_feedback.doc(responses={200: "POST ACCEPTED", 204: "ERROR! ID not exists", 400: "ERROR! ID is not int / ERROR! there is more than one true value"})
class Feedback(Resource):
    @ns_feedback.expect(parser_fred)
    def post(self):
        args = parser_fred.parse_args()
        id = args['id_image']
        glioma = 1 if args['glioma'] else 0
        meningioma = 1 if args['meningioma'] else 0
        pituitary = 1 if args['pituitary'] else 0
        no_tumor = 1 if args['no_tumor'] else 0
        comment = args['comment']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id(CSV_FRED, id):
            return response_generation({"message": "ERROR! ID not exists"}, 204)
        if (glioma + meningioma + pituitary + no_tumor) > 1:
            return response_generation({"message": "ERROR! there is more than one true value"}, 400)
        append_feedback_fred(id, glioma, meningioma,
                             pituitary, no_tumor, comment)
        return response_generation({"message": "POST ACCEPTED"}, 200)


parser_wini = reqparse.RequestParser()

parser_wini.add_argument('id_image', type=int, help='Id_image')
parser_wini.add_argument('pneumonia', type=inputs.boolean, help='pneumonia')
parser_wini.add_argument(
    'no_pneumonia', type=inputs.boolean, help='no_pneumonia')
parser_wini.add_argument('comment', type=str, help='comment')


@ns_feedback.route("/wini")
@ns_feedback.doc(responses={200: "POST ACCEPTED", 204: "ERROR! ID not exists", 400: "ERROR! ID is not int / ERROR! there is more than one true value"})
class Predict(Resource):
    @ns_feedback.expect(parser_wini)
    def post(self):
        args = parser_wini.parse_args()
        id = args['id_image']
        pneumonia = 1 if args['pneumonia'] else 0
        no_pneumonia = 1 if args['no_pneumonia'] else 0
        comment = args['comment']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id(CSV_WINI, id):
            return response_generation({"message": "ERROR! ID not exists"}, 204)
        if (pneumonia + no_pneumonia) == 2:
            return response_generation({"message": "ERROR! there is more than one true value"}, 400)
        append_feedback_wini(id, pneumonia, no_pneumonia, comment)
        return response_generation({"message": "POST ACCEPTED"}, 200)


parser_lyso = reqparse.RequestParser()
parser_lyso.add_argument('id_image', type=int, help='id_image')
parser_lyso.add_argument('quiste', type=inputs.boolean, help='quiste')
parser_lyso.add_argument('piedra', type=inputs.boolean, help='piedra')
parser_lyso.add_argument('tumor', type=inputs.boolean, help='tumor')
parser_lyso.add_argument('normal', type=inputs.boolean, help='normal')
parser_lyso.add_argument('comment', type=str, help='comment')


@ns_feedback.route("/lyso")
@ns_feedback.doc(responses={200: "POST ACCEPTED", 204: "ERROR! ID not exists", 400: "ERROR! ID is not int / ERROR! there is more than one true value"})
class Feedback(Resource):
    @ns_feedback.expect(parser_lyso)
    def post(self):
        args = parser_lyso.parse_args()
        id = args['id_image']
        quiste = 1 if args['quiste'] else 0
        piedra = 1 if args['piedra'] else 0
        tumor = 1 if args['tumor'] else 0
        normal = 1 if args['normal'] else 0
        comment = args['comment']
        is_int = isinstance(id, int)
        if not is_int:
            return response_generation({"message": "ERROR! ID is not int"}, 400)
        if not exists_id(CSV_LYSO, id):
            return response_generation({"message": "ERROR! ID not exists"}, 204)
        if (quiste + piedra + tumor + normal) > 1:
            return response_generation({"message": "ERROR! there is more than one true value"}, 400)
        append_feedback_lyso(id, quiste, piedra, tumor, normal, comment)
        return response_generation({"message": "POST ACCEPTED"}, 200)
