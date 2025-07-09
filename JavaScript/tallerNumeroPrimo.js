let num = parseInt(prompt("Ingresa un número:")); 
let esPrimo = true; 

if (num <= 1) { 
  esPrimo = false; 
} else { 
  for (let i = 2; i <= Math.sqrt(num); i++) { 
    if (num % i === 0) { 
      esPrimo = false; 
      break; 
    } 
  } 
} 
if (esPrimo) { 
  console.log("Es primo"); 
} else { 
  console.log("No es primo"); 
} 
