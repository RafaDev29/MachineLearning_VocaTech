from flask import jsonify, request
from src.modules.test_basic.service import predict_areas

def submit_test():
    try:
        data = request.get_json()  # Obtener los datos enviados en formato JSON
        predictions = predict_areas(data)  # Hacer las predicciones de áreas
        return jsonify({"message": "Datos ingresados correctamente", "status": True, "data": predictions}), 201
    except Exception as e:
        return jsonify({"message": str(e), "status": False, "data": None}), 500
