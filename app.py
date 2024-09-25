from flask import Flask
from src.modules.test_basic.routes import test_basic_bp  # Importamos el blueprint de TestBasic

app = Flask(__name__)

# Registrar el blueprint del módulo TestBasic
app.register_blueprint(test_basic_bp, url_prefix='/api/v1/test_basic')
 
@app.errorhandler(404)
def not_found(e):
    return {"message": "Resource not found", "status": False, "data": None}, 404

if __name__ == '__main__':
    app.run(debug=True)
