function reverse (str) {
   
    if (str === "") {
        return "";
    } else {
        return reverse(str.substr(1)) + str.charAt(0);
    }
}
var a=prompt("inserta una palabra: ");
let reverseStringIs = reverse(a);
alert(reverseStringIs);