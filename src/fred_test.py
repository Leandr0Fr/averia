import unittest
from app import app
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
        with open('image_test/no_tumor.jpg', 'rb') as image_file:
            response = self.app.post('/predict/fred', data={'image': (image_file, 'test.jpg')})
        self.assertEqual(response.status_code, 200)

    def test_predict_invalid_file(self):
        # Simula una solicitud POST con un archivo invalido
        with open('image_test/invalid.txt', 'rb') as image_file:
            response = self.app.post('/predict/fred', data={'image': (image_file, 'test.txt')})
        self.assertEqual(response.status_code, 418)

    def test_predict_no_image(self):
        # Simula una solicitud POST sin envio de imagen
        response = self.app.post('/predict/fred')
        self.assertEqual(response.status_code, 400)

    def test_predict_void(self):
        response = self.app.post('/predict/fred', data={'image': ''})
        self.assertEqual(response.status_code, 400)

    def test_predict_none(self):
        response = self.app.post('/predict/fred', data={'image': None})
        self.assertEqual(response.status_code, 400)

    def test_predict_no_tumor(self):
        # Simula una solicitud POST con una imagen y retorna no_tumor
        with open('image_test/no_tumor.jpg', 'rb') as image_file:
            response = self.app.post('/predict/fred', data={'image': (image_file, 'test.jpg')})
            data = response.get_json()
            result = data["no_tumor"]
            self.assertGreater(result, 95)

    def test_predict_glioma(self):
        # Simula una solicitud POST con una imagen y retorna Glioma
        with open('image_test/glioma.jpg', 'rb') as image_file:
            response = self.app.post('/predict/fred', data={'image': (image_file, 'test.jpg')})
            data = response.get_json()
            result = data["glioma"]
            self.assertGreater(result, 95)

    def test_predict_meningioma(self):
        # Simula una solicitud POST con una imagen y retorna Glioma
        with open('image_test/meningioma.jpg', 'rb') as image_file:
            response = self.app.post('/predict/fred', data={'image': (image_file, 'test.jpg')})
            data = response.get_json()
            result = data["meningioma"]
            self.assertGreater(result, 95)

    def test_predict_pituitary(self):
        # Simula una solicitud POST con una imagen y retorna Glioma
        with open('image_test/pituitary.jpg', 'rb') as image_file:
            response = self.app.post('/predict/fred', data={'image': (image_file, 'test.jpg')})
            data = response.get_json()
            result = data["pituitary"]
            self.assertGreater(result, 95)   
            
if __name__ == '__main__':
    unittest.main()