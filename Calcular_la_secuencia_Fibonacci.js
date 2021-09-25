

 function fibo(n) {
    return n < 2 ? n : fibo(n - 1) + fibo(n - 2)

}
var n=prompt("inserta tu numero: ");
alert (fibo(n));