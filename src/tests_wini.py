import unittest
from app import app

class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

## Test Wini

    def test_predict_valid_image(self): #1
        # Simula una solicitud POST con una imagen válida
        with open('image_test/neumonia_test.jpeg', 'rb') as image_file:
            response = self.app.post('/predict/wini', data={'image': (image_file, 'test.jpg')})
        self.assertEqual(response.status_code, 200)

    def test_predict_invalid_file(self): #2
        # Simula una solicitud POST con un archivo invalido
        with open('image_test/invalid.txt', 'rb') as image_file:
            response = self.app.post('/predict/wini', data={'image': (image_file, 'test.txt')})
        self.assertEqual(response.status_code, 418)

    def test_predict_no_image(self): #3
        # Simula una solicitud POST sin envio de imagen
        response = self.app.post('/predict/wini')
        self.assertEqual(response.status_code, 400)

    def test_predict_void(self): #4
        response = self.app.post('/predict/wini', data={'image': ''})
        self.assertEqual(response.status_code, 400)

    def test_predict_none(self): #5
        response = self.app.post('/predict/wini', data={'image': None})
        self.assertEqual(response.status_code, 400)

    def test_predict_pneumonia(self): #6
         # Simula una solicitud POST con una imagen válida
         with open('image_test/neumonia2_test.jpeg', 'rb') as image_file:
            response = self.app.post('/predict/wini', data={'image': (image_file, 'test.jpg')})
            data = response.get_json()
            result = data["pneumonia"]
            self.assertGreater(result, 95)

    def test_predict_notPneumonia(self): #7
         # Simula una solicitud POST con una imagen válida
         with open('image_test/NoNeumonia_test.jpeg', 'rb') as image_file:
            response = self.app.post('/predict/wini', data={'image': (image_file, 'test.jpg')})
            data = response.get_json()
            result = data["no_pneumonia"]
            self.assertGreater(result, 95)

    def test_none_fiebre(self):
        data = {'image': None,'puntada_lateral': None,'fiebre': None, 'dificultad_respiratoria': None}
        response = self.app.post('/predict/wini', json=data)
        response_data = response.get_json()
        self.assertIsNone(response_data.get("fiebre"))


    def test_void_fiebre(self):
        data = {'image': None,'puntada_lateral': None,'fiebre': "", 'dificultad_respiratoria': None}
        response = self.app.post('/predict/wini', json=data)
        response_data = response.get_json()
        self.assertIsNone(response_data.get("fiebre"))

    
    def test_invalid_fiebre(self):
        data = {'image': None,'puntada_lateral': None,'fiebre': 1, 'dificultad_respiratoria': None}
        response = self.app.post('/predict/wini', json=data)
        response_data = response.get_json()

        fiebre = type(response_data.get("fiebre"))

        if(isinstance(fiebre, bool)):
            self.assertFalse(True)
        else:
            self.assertFalse(False)

    def test_true_fiebre(self):
        data = {'image': None,'puntada_lateral': None,'fiebre': True, 'dificultad_respiratoria': None}
        response = self.app.post('/predict/wini', json=data)
        response_data = response.get_json()
        fiebre = type(response_data.get("fiebre"))
        self.assertTrue(fiebre)

    def test_false_fiebre(self):
        data = {'image': None,'puntada_lateral': None,'fiebre': False, 'dificultad_respiratoria': None}
        response = self.app.post('/predict/wini', json=data)
        response_data = response.get_json()
        fiebre = type(response_data.get("fiebre"))
        self.assertFalse(fiebre)

    
        


if __name__ == '__main__':
    unittest.main()