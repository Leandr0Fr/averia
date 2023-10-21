import numpy as np
import tensorflow
from PIL import Image

def prediction_tumor():
    #Carga el modelo.
    model = tensorflow.keras.models.load_model("routes/tumor_model.h5")
    img = Image.open("routes/image.png").convert("L")
    #Transforma la imagen para que coincidan con el modelo. 
    img = img.resize((224, 224)) 
    img = np.array(img)
    img = img / 255.0
    img = img.reshape((1,224,224,1))
    #Predice el modelo 
    predict = model.predict(img)[0]
    #Como son 4 clases, entonces es una lista de 4 elementos.
    class_labels = ["Glioma", "Meningioma", "Pituitary", "No_tumor"]
    #Genera una lista con los % de acierto.
    probabilities = [(prob * 100) for prob in predict]
    return list(zip(class_labels, probabilities))

def prediction_pneumonia():
      #Carga el modelo.
    model = tensorflow.keras.models.load_model("routes/neumonia-resnet.h5")
    img = Image.open("routes/image.png").convert("L")
    #Transforma la imagen para que coincidan con el modelo. 
    img = img.resize((224, 224)) 
    img = np.array(img)
    img = img / 255.0
    #Predice el modelo 
    predict = model.predict(img)[0]
    #Como son 4 clases, entonces es una lista de 4 elementos.
    class_labels = ["Pneumonia", "No_Pneumonia"]
    #Genera una lista con los % de acierto.
    probabilities = [(prob * 100) for prob in predict]
    return list(zip(class_labels, probabilities))