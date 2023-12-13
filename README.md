# API REST: Modelos de IA.

Esta API forma parte de un proyecto sobre detección de enfermedades mediante imágenes utilizando modelos de IA.

Los modelos ya están entrenados y exportados. El desarrollo de los modelos se puede ver [aquí](https://github.com/xebertz/tp-principal-grupo-0-lcs).

Las imágenes se almacenan adjuntas con los datos en un CSV. Se realizó de esta manera porque implementar una base de datos era un exceso para el contexto en el que fue desarrollada la API.

La API no fue desarrollada para uso directo. Fue planificada para ser consumida por un backend, por esto mismo no generamos un ID para cada imagen, ya que la ID ya fue generada anteriormente.

### Configuración inicial

1.- Clonar el repositorio:

    git clone https://github.com/Leandr0Fr/averia.git

2.- Crear un entorno virtual:

    virtualenv nombre_entorno | python -m venv nombre_entorno

3.- Activar el entorno:

    .\env\Scripts\activate

4.- Instalar librerias:

    (env) pip install -r requirements.txt

5.- Levantar servidor de desarrollador:

    (env) flask run