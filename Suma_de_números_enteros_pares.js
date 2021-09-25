function sumaDeLosParesDel0Al(x){
    var suma = 0
    for (var i=1; i<x; i++){
      if (i%2 == 0) {
        suma += i
      }
    }
    return suma
  }
  
alert(sumaDeLosParesDel0Al(10));
