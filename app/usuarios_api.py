from flask import Blueprint, jsonify, request
from services.usuario_service import ##importar banco e serviços


usuario_app = Blueprint('usuario_app', __name__, template_folder='templates')

@usuario_app.route('/login', methods=['GET'])
def autenticar():
   pass
