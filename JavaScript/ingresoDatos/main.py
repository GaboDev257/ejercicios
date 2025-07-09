from flask import Flask, request
from flask_cors import CORS 
import csv
app = Flask(__name__)
CORS(app)
@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    nombre = data.get('nombre', '').strip()
    correo = data.get('correo', '').strip()

# Validar que los campos no estén vacíos
    if not nombre or not correo:
        return "Faltan datos", 400

    with open('estudiantes.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, correo])
    return "Registro exitoso"

if __name__ == '__main__':
    app.run(debug=True)