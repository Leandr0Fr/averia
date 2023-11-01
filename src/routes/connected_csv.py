import pandas as pd
import os
from .routes import *
def exists_id(csv, id):
    df = pd.read_csv(csv)
    list_id = df['id'].tolist()
    return id in list_id

#wini

def append_predict_wini(id, imagen, puntada_lateral, fiebre, dificultad_respiratoria):
    df = pd.read_csv(CSV_WINI)
    new_row = pd.DataFrame({'id': [id], 'imagen': [imagen], 'puntada_lateral': [puntada_lateral],
                            'fiebre': [fiebre], 'dificultad_respiratoria': [dificultad_respiratoria],
                            'pneumonia': [''], 'no_pneumonia': [''], 'comment': ['']})

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_WINI, index=False, float_format='%.0f')


def append_feedback_wini(id, pneumonia, no_pneumonia, comment):
    df = pd.read_csv(CSV_WINI)

    df.loc[df['id'] == id, 'pneumonia'] = pneumonia
    df.loc[df['id'] == id, 'no_pneumonia'] = no_pneumonia
    df.loc[df['id'] == id, 'comment'] = comment

    df.to_csv(CSV_WINI, index=False, float_format='%.0f')

#fred

def append_predict_fred(id, imagen, debilidad_focal, convulsiones, perdida_visual):
    df = pd.read_csv(CSV_FRED)
    new_row = pd.DataFrame({'id': [id], 'imagen': [imagen], 'debilidad_focal': [debilidad_focal],
                            'convulsiones': [convulsiones], 'perdida_visual': [perdida_visual],
                            'glioma': [''], 'meningioma': [''], 'pituitary': [''], 'no_tumor': [''], 'comment': ['']})

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FRED, index=False, float_format='%.0f')


def append_feedback_fred(id, glioma, meningioma, pituitary, no_tumor, comment):
    df = pd.read_csv(CSV_FRED)

    df.loc[df['id'] == id, 'glioma'] = glioma
    df.loc[df['id'] == id, 'meningioma'] = meningioma
    df.loc[df['id'] == id, 'pituitary'] = pituitary
    df.loc[df['id'] == id, 'no_tumor'] = no_tumor
    df.loc[df['id'] == id, 'comment'] = comment

    df.to_csv(CSV_FRED, index=False, float_format='%.0f')

#lyso

def append_predict_lyso(id, imagen, hermaturia, dolor_lumbar, dolor_abdominal, fiebre, perdida_peso):
    df = pd.read_csv(CSV_LYSO)
    new_row = pd.DataFrame({'id': [id], 'imagen': [imagen], 'hermaturia': [hermaturia],
                            'dolor_lumbar': [dolor_lumbar], 'dolor_abdominal': [dolor_abdominal],
                            'fiebre': [fiebre], 'perdida_peso': [perdida_peso],
                            'quiste': [''], 'piedra': [''], 'tumor': [''], 'normal': [''] , 'comment': ['']})
    
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_LYSO, index=False, float_format='%.0f')


def append_feedback_lyso(id, quiste, piedra, tumor, normal, comment):
    df = pd.read_csv(CSV_LYSO)

    df.loc[df['id'] == id, 'quiste'] = quiste
    df.loc[df['id'] == id, 'piedra'] = piedra
    df.loc[df['id'] == id, 'tumor'] = tumor
    df.loc[df['id'] == id, 'normal'] = normal
    df.loc[df['id'] == id, 'comment'] = comment

    df.to_csv(CSV_LYSO, index=False, float_format='%.0f')

#delete
def delete_id(id, route_csv, model):
    df = pd.read_csv(route_csv)
    
    row = df[df['id'] == id]

    if not row.empty:
        image = row['imagen'].values[0]
        route = f"csv/{model}/{image}"
        if os.path.exists(route):
            os.remove(route)
    df = df[df['id'] != id]

    df.to_csv(route_csv, index=False, float_format='%.0f')

def delete_all(route_csv, name):
    route_images = f"csv/{name}/images"
    df = pd.read_csv(route_csv)
    df = pd.DataFrame(columns=df.columns)
    for filename in os.listdir(route_images):
        if filename.endswith('.txt'):
            continue
        file_path = os.path.join(route_images, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    df.to_csv(route_csv, index=False)