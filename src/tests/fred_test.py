import os, sys

current_route = os.path.dirname(os.path.abspath(__file__))
route_src = os.path.abspath(os.path.join(current_route, '..'))
sys.path.append(route_src)

import unittest
from app import app
from routes import *
from app.utils.connected_csv import delete_all, delete_id
from app.utils.routes import *

class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ping_endpoint(self):
        # Realiza un ping al servidor
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)

    def test_predict_valid_image(self):
        # Simula una solicitud POST con una imagen válida
        with open(GLIOMA_IMAGE, 'rb') as image_file:
            response = self.app.post(
                '/predict/fred', data={'image': image_file, 'id_image': 0})
            delete_id(0,CSV_FRED, "fred")
        self.assertEqual(response.status_code, 200)

    def test_predict_invalid_file(self):
        # Simula una solicitud POST con un archivo invalido
        with open('image_test/invalid.txt', 'rb') as image_file:
            response = self.app.post(
                '/predict/fred', data={'image': image_file, 'id_image': 0})
        self.assertEqual(response.status_code, 418)

    def test_predict_no_image(self):
        # Simula una solicitud POST sin envio de imagen
        response = self.app.post('/predict/fred')
        self.assertEqual(response.status_code, 404)

    def test_predict_void(self):
        response = self.app.post('/predict/fred', data={'image': '', 'id_image': 0})
        self.assertEqual(response.status_code, 404)

    def test_predict_none(self):
        response = self.app.post('/predict/fred', data={'image': None, 'id_image': 0})
        self.assertEqual(response.status_code, 404)

    def test_predict_no_tumor(self):
        # Simula una solicitud POST con una imagen y retorna no_tumor
        with open('image_test/no_tumor.jpg', 'rb') as image_file:
            response = self.app.post(
                '/predict/fred', data={'image': image_file, 'id_image': 0})
            data = response.get_json()
            result = data["no_tumor"]
            delete_id(0,CSV_FRED, "fred")
            self.assertGreater(result, 95)

    def test_predict_glioma(self):
        # Simula una solicitud POST con una imagen y retorna Glioma
        with open('image_test/glioma.jpg', 'rb') as image_file:
            response = self.app.post(
                '/predict/fred', data={'image': image_file, 'id_image': 0})
            data = response.get_json()
            result = data["glioma"]
            delete_id(0,CSV_FRED, "fred")
            self.assertGreater(result, 95)

    def test_predict_meningioma(self):
        # Simula una solicitud POST con una imagen y retorna Glioma
        with open('image_test/meningioma.jpg', 'rb') as image_file:
            response = self.app.post(
                '/predict/fred', data={'image': image_file, 'id_image': 0})
            data = response.get_json()
            result = data["meningioma"]
            delete_id(0,CSV_FRED, "fred")
            self.assertGreater(result, 95)

    def test_predict_pituitary(self):
        # Simula una solicitud POST con una imagen y retorna Glioma
        with open('image_test/pituitary.jpg', 'rb') as image_file:
            response = self.app.post(
                '/predict/fred', data={'image': image_file, 'id_image': 0})
            data = response.get_json()
            result = data["pituitary"]
            delete_id(0,CSV_FRED, "fred")
            self.assertGreater(result, 95)
    
if __name__ == '__main__':
    unittest.main()
