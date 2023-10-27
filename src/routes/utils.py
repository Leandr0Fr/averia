import pandas as pd
#falta codigo defensivo a todas las def
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

def append_feedback_wini(id, pneumonia, no_pneumonia):
    df = pd.read_csv("csv/wini.csv")
    
    df.loc[df['id'] == id, 'pneumonia'] = pneumonia
    df.loc[df['id'] == id, 'no_pneumonia'] = no_pneumonia

    df.to_csv("csv/wini.csv", index=False, float_format='%.0f')

def append_predict_fred(id, imagen, debilidad_focal, convulsiones, perdida_visual):
    df = pd.read_csv("csv/fred.csv")
    new_row = pd.DataFrame({'id' : [id], 'imagen' : [imagen], 'debilidad_focal' : [debilidad_focal],
                             'convulsiones' : [convulsiones], 'perdida_visual' : [perdida_visual],
                             'glioma' : [''], 'meningioma' : [''], 'pituitary' : [''], 'no_tumor' : ['']})
    
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('csv/fred.csv', index=False)

def append_feedback_fred(id, glioma, meningioma, pituitary, no_tumor):
    df = pd.read_csv("csv/fred.csv")
    
    df.loc[df['id'] == id, 'glioma'] = glioma
    df.loc[df['id'] == id, 'meningioma'] = meningioma
    df.loc[df['id'] == id, 'pituitary'] = pituitary
    df.loc[df['id'] == id, 'no_tumor'] = no_tumor

    df.to_csv("csv/fred.csv", index=False, float_format='%.0f')