import  os

current_route = os.path.dirname(os.path.abspath(__file__))
app_route = os.path.abspath(os.path.join(current_route, '..'))
src_route = os.path.abspath(os.path.join(app_route, '..'))

#rutas relacionadas con el modelo fred
MODEL_FRED = f"{src_route}/app/models_ia/tumor_model.h5"
CSV_FRED = f"{src_route}/app/csv/fred/fred.csv"
IMAGES_FRED = f"{src_route}/app/csv/fred/images"
FOLDER_FRED = f"{src_route}/app/csv/fred"
DOWNLOAD_FRED_ROUTE = f"{src_route}/download/fred.zip"
#rutas relacionadas con el modelo wini
MODEL_WINI = f"{src_route}/app/models_ia/neumonia-resnet.h5"
CSV_WINI = f"{src_route}/app/csv/wini/wini.csv"
IMAGES_WINI = f"{src_route}/app/csv/wini/images"
FOLDER_WINI = f"{src_route}/app/csv/wini"
DOWNLOAD_WINI_ROUTE = f"{src_route}/download/wini.zip"
#rutas relacionadas con el modelo lyso
MODEL_LYSO = f"{src_route}/app/models_ia/cnn-riniones.h5"
CSV_LYSO = f"{src_route}/app/csv/lyso/lyso.csv"
IMAGES_LYSO = f"{src_route}/app/csv/lyso/images"
FOLDER_LYSO = f"{src_route}/app/csv/lyso"
DOWNLOAD_LYSO_ROUTE = f"{src_route}/download/lyso.zip"

CSV_ROUTE = f"{src_route}/app/csv"