import pandas as pd
#falta codigo defensivo a todas las def
def exists_id(csv, id):
    df = pd.read_csv(csv)
    list_id = df['id'].tolist()
    return id in list_id

def append_predict_wini(id, imagen, puntada_lateral, fiebre, dificultad_respiratoria):
    df = pd.read_csv("wini.csv")
    new_row = pd.DataFrame({'id' : [id], 'imagen' : [imagen], 'puntada_lateral' : [puntada_lateral],
                             'fiebre' : [fiebre], 'dificultad_respiratoria' : [dificultad_respiratoria],
                             'pneumonia' : [''], 'no_pneumonia' : ['']})
    
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('wini.csv', index=False)

def append_feedback_wini(id, pneumonia, no_pneumonia):
    df = pd.read_csv("wini.csv")
    
    df.loc[df['id'] == id, 'pneumonia'] = pneumonia
    df.loc[df['id'] == id, 'no_pneumonia'] = no_pneumonia

    df.to_csv("wini.csv", index=False, float_format='%.0f')
