#Backend en Python con Flask (CRUD completo)
 
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv, os
 
app = Flask(__name__)
CORS(app)  # Permite solicitudes desde otros orígenes
ARCHIVO = "estudiantes.csv"
 
def leer_estudiantes():
   if not os.path.exists(ARCHIVO):
       return []
   with open(ARCHIVO, newline='') as f:
       reader = csv.reader(f)
       return [{"nombre": r[0], "correo": r[1], "carrera": r[2]} for r in reader]
 
def guardar_estudiantes(lista):
   with open(ARCHIVO, "w", newline='') as f:
       writer = csv.writer(f)
       for est in lista:
          writer.writerow([est["nombre"], est["correo"], est["carrera"]])
 
@app.route("/registrar", methods=["POST"])
def registrar():
   data = request.get_json()
   if not data or not all(k in data for k in ("nombre", "correo", "carrera")):
       return "Datos incompletos", 400
   estudiantes = leer_estudiantes()
   estudiantes.append(data)
   guardar_estudiantes(estudiantes)
   return "Estudiante registrado"
 
@app.route("/estudiantes", methods=["GET"])
def listar():
   return jsonify(leer_estudiantes())
 
@app.route("/eliminar/<int:indice>", methods=["DELETE"])
def eliminar(indice):
   estudiantes = leer_estudiantes()
   if 0 <= indice < len(estudiantes):
      estudiantes.pop(indice)
      guardar_estudiantes(estudiantes)
      return "Estudiante eliminado"
   return "Índice inválido", 400
 
@app.route("/eliminar_todos", methods=["DELETE"])
def eliminar_todos():
   open(ARCHIVO, "w").close()
   return "Todos los registros han sido eliminados"
 
@app.route("/buscar/<nombre>", methods=["GET"])
def buscar(nombre):
   nombre = nombre.lower()
   estudiantes = leer_estudiantes()
   resultado = [e for e in estudiantes if nombre in e["nombre"].lower()]
   return jsonify(resultado)
 
if __name__ == "__main__":
  app.run(debug=True)