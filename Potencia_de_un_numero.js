var a=prompt("inserta tu numero: ");
var b=prompt("inserta la potencia: ");
function potencia (a, b){

    if(b==0){
        return 1;
    }
    else{
        return a*potencia(a,b-1);
    }
   
}

 alert (potencia(a,b));
 