estudiantes = [
    {"nombre": "Ana", "edad": 20, "curso": "Matemáticas"},
    {"nombre": "Luis", "edad": 22, "curso": "Historia"},
    {"nombre": "María", "edad": 21, "curso": "Ciencias"},
    {"nombre": "Pedro", "edad": 23, "curso": "Literatura"},
    {"nombre": "Laura", "edad": 20, "curso": "Física"}
]

estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["edad"])
resultado = [f'{x["nombre"]} - {x["edad"]} años - {x["curso"]}' for x in estudiantes_ordenados]
for r in resultado:
    print(r)