import os, sys

current_route = os.path.dirname(os.path.abspath(__file__))
route_src = os.path.abspath(os.path.join(current_route, '..'))
sys.path.append(route_src)

import unittest
from app import app
from routes import *
from app.utils.connected_csv import delete_id
from app.utils.routes import *

class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

# Test Wini

    def test_predict_valid_image(self):  # 1
        # Simula una solicitud POST con una imagen válida
        with open(NEUMONIA_IMAGE, 'rb') as image_file:
            response = self.app.post(
                '/predict/wini', data={'image': image_file, 'id_image': 0})
            delete_id(0,CSV_WINI, "wini")
        self.assertEqual(response.status_code, 200)

    def test_predict_invalid_file(self):  # 2
        # Simula una solicitud POST con un archivo invalido
        with open(INVALID_FILE, 'rb') as image_file:
            response = self.app.post(
                '/predict/wini', data={'image': image_file, 'id_image': 0})
            delete_id(0,CSV_WINI, "wini")
        self.assertEqual(response.status_code, 418)

    def test_predict_no_image(self):  # 3
        # Simula una solicitud POST sin envio de imagen
        response = self.app.post('/predict/wini')
        self.assertEqual(response.status_code, 404)

    def test_predict_void(self):  # 4
        response = self.app.post('/predict/wini', data={'image': '', 'id_image': 0})
        self.assertEqual(response.status_code, 404)

    def test_predict_none(self):  # 5
        response = self.app.post('/predict/wini', data={'image': None, 'id_image': 0})
        self.assertEqual(response.status_code, 404)

    def test_predict_pneumonia(self):  # 6
        # Simula una solicitud POST con una imagen válida
        with open(NEUMONIA_IMAGE_2, 'rb') as image_file:
            response = self.app.post(
                '/predict/wini', data={'image': image_file, 'id_image': 0})
            data = response.get_json()
            result = data["pneumonia"]
            delete_id(0,CSV_WINI, "wini")
            self.assertGreater(result, 95)

    def test_predict_notPneumonia(self):  # 7
        # Simula una solicitud POST con una imagen válida
        with open(NO_NEUMONIA_IMAGE, 'rb') as image_file:
            response = self.app.post(
                '/predict/wini', data={'image': image_file, 'id_image': 0})
            data = response.get_json()
            result = data["no_pneumonia"]
            delete_id(0,CSV_WINI, "wini")
            self.assertGreater(result, 95)

if __name__ == '__main__':
    unittest.main()
