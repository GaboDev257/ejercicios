let tareas = []; 

function  guardarTarea() {
  localStorage.setItem("tareas", JSON.stringify(tareas));
}

document.getElementById("addTask").addEventListener("click", function() { 
  let texto = document.getElementById("nuevaTarea").value; 
  if (texto) { 
    tareas.push(texto)
    guardarTarea(); // Guarda las tareas en localStorage 
    mostrarTareas(); 
    document.getElementById("nuevaTarea").value = ""; 
  } 
}); 
 
function mostrarTareas() { 
  let lista = document.getElementById("listaTareas"); 
  lista.innerHTML = ""; 
  tareas.forEach(function(tarea, index) { 
    let li = document.createElement("li"); 
    li.textContent = tarea + ""; 
    let botonEliminar = document.createElement("button");
    botonEliminar.textContent = "Eliminar";
    botonEliminar.addEventListener("click", function() {
      tareas.splice(index, 1); // Elimina la tarea seleccionada
      guardarTarea(); // Guarda las tareas actualizadas en localStorage
      mostrarTareas(); // Actualiza la lista de tareas
    });
    li.appendChild(botonEliminar); // Agrega el botón de eliminar a la tarea
    lista.appendChild(li); 
    }); 
} 

function cargarTareas() {
  let tareasGuardadas = localStorage.getItem("tareas");
  if (tareasGuardadas) {
    tareas = JSON.parse(tareasGuardadas);
    mostrarTareas();
  }
}
window.onload = cargarTareas; // Carga las tareas al iniciar la página
