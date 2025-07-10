//console.log(`Hola, mi nombre es ${firstName} y tengo ${edad} años.`);
function validaUsuario(usuario) {
    if (usuario.age >= 18) {
        console.log("Usuario válido");
        return "Hola, ".concat(usuario.firstName, " tienes ").concat(usuario.age, " a\u00F1os. Usuario v\u00E1lido.");
    }
    else {
        console.log("Usuario no válido");
        return "Hola, ".concat(usuario.firstName, " tienes ").concat(usuario.age, " a\u00F1os. Usuario no v\u00E1lido.");
    }
}
console.log(validaUsuario({ firstName: "Juan", age: 20 }));
