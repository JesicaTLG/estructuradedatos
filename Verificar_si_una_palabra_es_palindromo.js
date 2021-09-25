function palindro(p){
    return p.split('').reverse().join('')==p;

}
var p=prompt("inserta una palabra: ");
alert( palindro(p) );