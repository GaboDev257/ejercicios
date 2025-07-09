document.getElementById("formulario").addEventListener("submit", function(e) {
    e.preventDefault();
    const nombre = document.getElementById("nombre").value.trim();
    const correo = document.getElementById("correo").value.trim();

    if (nombre === "" || correo === "") {
      document.getElementById("mensaje").textContent = "Todos los campos son obligatorios.";
      return;
    }

    fetch("http://localhost:5000/registrar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nombre, correo })
    })
    .then(response => response.text())
    .then(data => {
      document.getElementById("mensaje").textContent = data;
      document.getElementById("formulario").reset();
    })
    .catch(error => {
      document.getElementById("mensaje").textContent = "Error al registrar.";
      console.error(error);
    });
  });