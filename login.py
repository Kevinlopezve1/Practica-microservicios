from flask import Flask, jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesion'

# Configuración de flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

usuarios = {
    "usuario1": {"password": "password123"},
    "usuario2": {"password": "password456"},
}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in usuarios and usuarios[username]['password'] == password:
        user = User(username)
        login_user(user)
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    return jsonify({"mensaje": "Usuario o contraseña incorrectos"}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"mensaje": "Sesión cerrada"}), 200

@app.route('/api/usuarios', methods=['GET'])
@login_required
def obtener_usuarios():
    return jsonify({"usuarios": list(usuarios.keys())})

@app.route('/health', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy", "service": "usuarios"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)