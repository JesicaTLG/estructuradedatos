  

   function inverse(num) {
    let reversed = 0;
    
    
    while(num > 0) {
        reversed = reversed * 10;
        reversed = reversed + (num % 10);
        num = parseInt(num / 10);
    
}
alert( 'el numero 12345 Invertido es: '+ reversed);
}

inverse(12345);