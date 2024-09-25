import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Función para entrenar los modelos desde el CSV
def train_model_from_csv():
    # Cargar el archivo CSV
    df = pd.read_csv('src/modules/test_basic/simulacion_test_vocacional.csv', encoding='ISO-8859-1')


    # Seleccionar las columnas de preguntas (X) y áreas (y)
    X = df.iloc[:, 1:11]  # Preguntas del cuestionario
    y_area1 = df['Área 1']  # Primera área profesional
    y_area2 = df['Área 2']  # Segunda área profesional

    # Convertir las respuestas (A, B, C, D, E) a valores numéricos usando LabelEncoder
    encoder = LabelEncoder()
    for column in X.columns:
        X[column] = encoder.fit_transform(X[column])

    # Dividir los datos para entrenar dos modelos: uno para cada área
    X_train, X_test, y_train1, y_test1 = train_test_split(X, y_area1, test_size=0.2, random_state=42)
    X_train, X_test, y_train2, y_test2 = train_test_split(X, y_area2, test_size=0.2, random_state=42)

    # Entrenar modelo de Random Forest para Área 1
    model_area1 = RandomForestClassifier()
    model_area1.fit(X_train, y_train1)

    # Entrenar modelo de Random Forest para Área 2
    model_area2 = RandomForestClassifier()
    model_area2.fit(X_train, y_train2)

    # Guardar los modelos en archivos .pkl dentro de la carpeta test_basic
    joblib.dump(model_area1, 'src/modules/test_basic/model_area1.pkl')
    joblib.dump(model_area2, 'src/modules/test_basic/model_area2.pkl')

    print("Modelos entrenados y guardados en 'src/modules/test_basic/'.")

# Llamar a la función para entrenar y guardar los modelos
if __name__ == "__main__":
    train_model_from_csv()
