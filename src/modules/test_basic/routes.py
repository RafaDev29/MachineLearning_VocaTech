from flask import Blueprint
from src.modules.test_basic.controller import submit_test

# Crear el blueprint para el módulo TestBasic
test_basic_bp = Blueprint('test_basic', __name__)

# Definir las rutas
@test_basic_bp.route('/submit', methods=['POST'])
def post_test():
    return submit_test()
