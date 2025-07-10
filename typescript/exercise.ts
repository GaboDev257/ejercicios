interface User {
    firstName: string;
    age: number;
}

//console.log(`Hola, mi nombre es ${firstName} y tengo ${edad} años.`);

function validaUsuario(usuario: User): string {
    if (usuario.age >= 18) {
        console.log("Usuario válido");
        return `Hola, ${usuario.firstName} tienes ${usuario.age} años. Usuario válido.`;
    } else {
        console.log("Usuario no válido");
        return `Hola, ${usuario.firstName} tienes ${usuario.age} años. Usuario no válido.`;
    }
}
console.log(validaUsuario({ firstName: "Juan", age: 20 }));
