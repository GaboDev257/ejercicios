function suma(a, b) {
    return a + b;
}

console.log(suma(9, 6));

const miLista = ["pera", "manzana", "naranja", "kiwi"];
const alumno = {
    nombre: "Juan",
    edad: 20,
    };

console.log(miLista[2]);
console.log(alumno.nombre);

let base = parseFloat(prompt("Ingresa la medida de la base"));
let altura = parseFloat(prompt("Ingresa la medida de la altura"));
let resultado = areaRectangulo(base, altura);

function areaRectangulo(base, altura) {
    return (base * altura);
}  
console.log("El área del rectángulo es: " + resultado);
