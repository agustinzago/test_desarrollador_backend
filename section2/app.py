from flask import Flask, request, jsonify
from functools import wraps
import sqlite3

app = Flask(__name__)


def autenticacion(f):
    @wraps(f)
    def funcion_decorada(*args, **kwargs):
        auth = request.authorization
        if not auth or not verificar_autenticacion(auth.username, auth.password):
            return jsonify({'message': '¡Autenticación requerida!'}), 401
        return f(*args, **kwargs)
    return funcion_decorada


def verificar_autenticacion(nombre_usuario, contraseña):
    conn = sqlite3.connect('ejemplo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ?",
                   (nombre_usuario,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario and usuario[3] == contraseña:
        return True
    return False


@app.route('/')
def indice():
    return jsonify({'message': 'Bienvenido a mi aplicación Flask!'})


@app.route('/auth')
@autenticacion
def ruta_protegida():
    return jsonify({'message': 'Bienvenido a la ruta protegida!'})


@app.route('/usuarios')
def obtener_informacion_usuario():
    id_usuario = request.args.get('id')
    if not id_usuario:
        return jsonify({'message': 'Se requiere un parámetro id!'}), 400

    conn = sqlite3.connect('ejemplo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    usuario = cursor.fetchone()

    conn.close()

    if not usuario:
        return jsonify({'message': 'Usuario no encontrado!'}), 404

    informacion_usuario = {
        'id': usuario[0],
        'nombre_usuario': usuario[1],
        'email': usuario[2]
    }

    return jsonify(informacion_usuario)


if __name__ == '__main__':
    app.run(debug=True)
