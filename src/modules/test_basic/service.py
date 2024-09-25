import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Cargar los modelos entrenados
model_area1 = joblib.load('src/modules/test_basic/model_area1.pkl')
model_area2 = joblib.load('src/modules/test_basic/model_area2.pkl')

# Cargar el LabelEncoder
encoder = LabelEncoder()

# Función para procesar las respuestas y hacer las predicciones
def predict_areas(data):
    # Extraer las respuestas de las preguntas
    answers = [data['question1'], data['question2'], data['question3'], data['question4'], 
               data['question5'], data['question6'], data['question7'], data['question8'], 
               data['question9'], data['question10']]
    
    # Codificar las respuestas (A, B, C, D, E) para que coincidan con el formato del entrenamiento
    encoded_answers = encoder.fit_transform(answers)
    reshaped_answers = np.array(encoded_answers).reshape(1, -1)
    
    # Predecir las áreas usando los modelos entrenados
    area1_prediction = model_area1.predict(reshaped_answers)[0]
    area2_prediction = model_area2.predict(reshaped_answers)[0]

    # Devolver las áreas predichas
    return {"area1": area1_prediction, "area2": area2_prediction}
