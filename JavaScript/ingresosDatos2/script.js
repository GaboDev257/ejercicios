const tabla = document.querySelector("#tabla tbody");
 
   function registrarEstudiante() {
     const nombre = document.getElementById("nombre").value.trim();
     const correo = document.getElementById("correo").value.trim();
     const carrera = document.getElementById("carrera").value.trim();
 
     if (!nombre || !correo || !carrera) {
      document.getElementById("mensaje").textContent = "Todos los campos son obligatorios.";
       return;
     }
 
    fetch("http://localhost:5000/registrar", {
       method: "POST",
       headers: { "Content-Type": "application/json" },
       body: JSON.stringify({ nombre, correo, carrera })
     })
     .then(res => res.text())
     .then(msg => {
      document.getElementById("mensaje").textContent = msg;
      limpiarFormulario();
      cargarEstudiantes();
     });
   }
 
   function cargarEstudiantes() {
     tabla.innerHTML = "";
     fetch("http://localhost:5000/estudiantes")
       .then(res => res.json())
      .then(estudiantes => {
        estudiantes.forEach((e, i) => {
           const fila = tabla.insertRow();
          fila.innerHTML = `
            <td>${e.nombre}</td>
            <td>${e.correo}</td>
            <td>${e.carrera}</td>
            <td><button onclick="eliminarEstudiante(${i})">Eliminar</button></td>
           `;
         });
       });
   }
 
   function eliminarEstudiante(indice) {
     fetch(`http://localhost:5000/eliminar/${indice}`, { method: "DELETE" })
       .then(res => res.text())
       .then(msg => {
        document.getElementById("mensaje").textContent = msg;
        cargarEstudiantes();
       });
   }
 
   function eliminarTodos() {
     if (!confirm("¿Seguro que deseas eliminar todos los registros?")) return;
 
    fetch("http://localhost:5000/eliminar_todos", { method: "DELETE" })
       .then(res => res.text())
       .then(msg => {
        document.getElementById("mensaje").textContent = msg;
        tabla.innerHTML = "";
       });
   }
 
   function buscarEstudiantes() {
     const nombre = document.getElementById("buscar").value.trim();
     if (!nombre) return cargarEstudiantes();
 
     tabla.innerHTML = "";
    fetch(`http://localhost:5000/buscar/${nombre}`)
       .then(res => res.json())
      .then(estudiantes => {
         if (estudiantes.length === 0) {
          document.getElementById("mensaje").textContent = "No se encontraron coincidencias.";
           return;
         }
        estudiantes.forEach((e, i) => {
           const fila = tabla.insertRow();
          fila.innerHTML = `
            <td>${e.nombre}</td>
            <td>${e.correo}</td>
            <td>${e.carrera}</td>
            <td><em>No editable</em></td>
           `;
         });
       });
   }
 
   function limpiarFormulario() {
    document.getElementById("nombre").value = "";
    document.getElementById("correo").value = "";
    document.getElementById("carrera").value = "";
   }