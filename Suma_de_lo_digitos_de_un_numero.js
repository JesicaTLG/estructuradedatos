var num=prompt("Ingrese un número: ");

function sumarDigitos (num) {
  if(0<num) {
    return (num%10) + sumarDigitos(Math.floor(num/10));
  }
  return num;
};

alert(sumarDigitos(num));