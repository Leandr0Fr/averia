import numpy as np
import tensorflow
from PIL import Image


def prediction_tumor(name):
    # Carga el modelo.
    model = tensorflow.keras.models.load_model("models_ia/tumor_model.h5")
    img = Image.open(f"csv/fred/images/{name}.png").convert("L")
    # Transforma la imagen para que coincidan con el modelo.
    img = img.resize((224, 224))
    img = np.array(img)
    img = img / 255.0
    img = img.reshape((1, 224, 224, 1))
    # Predice el modelo
    predict = model.predict(img)[0]
    # Como son 4 clases, entonces es una lista de 4 elementos.
    class_labels = ["Glioma", "Meningioma", "Pituitary", "No_tumor"]
    # Genera una lista con los % de acierto.
    probabilities = [(prob * 100) for prob in predict]
    return list(zip(class_labels, probabilities))


def prediction_pneumonia(name):
    # Carga el modelo.
    model = tensorflow.keras.models.load_model("models_ia/neumonia-resnet.h5")
    # Transforma la imagen para que coincidan con el modelo.
    img = Image.open(f"csv/wini/images/{name}.png").convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = img_array / 255
    # Realiza la predicción
    class_labels = ["pneumonia", "no_pneumonia"]
    predict = model.predict(np.expand_dims(img_array, axis=0))[0]
    probabilities = [(prob * 100) for prob in predict]
    return list(zip(class_labels, probabilities))

def prediction_kidney(name):
    # Carga el modelo.
    model = tensorflow.keras.models.load_model("models_ia/cnn-riniones.h5")
    # Transforma la imagen para que coincidan con el modelo.
    img = Image.open(f"csv/lyso/images/{name}.png").convert("L")
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = img_array / 255
    # Realiza la predicción
    class_labels = ["quiste", "piedra", "tumor", "normal"]
    predict = model.predict(np.expand_dims(img_array, axis=0))[0]
    probabilities = [(prob * 100) for prob in predict]
    return list(zip(class_labels, probabilities))
