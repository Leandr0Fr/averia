import pandas as pd

def exists_id(csv, id):
    df = pd.read_csv(csv)
    list_id = df['id'].tolist()
    return id in list_id

def append_predict_wini(id, imagen, puntada_lateral, fiebre, dificultad_respiratoria):
    df = pd.read_csv("csv/wini.csv")
    new_row = pd.DataFrame({'id' : [id], 'imagen' : [imagen], 'puntada_lateral' : [puntada_lateral],
                             'fiebre' : [fiebre], 'dificultad_respiratoria' : [dificultad_respiratoria],
                             'pneumonia' : [''], 'no_pneumonia' : ['']})
    
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('csv/wini.csv', index=False)