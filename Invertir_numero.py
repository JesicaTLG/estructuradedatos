def invertir(numero, invertido):
 
    (cociente, residuo) = divmod(numero, 10)
 
    if 0 == cociente:
        return invertido * 10 + residuo
    elif 0 == invertido:
        return invertir(cociente, residuo)
    else:
        return invertir(cociente, invertido * 10 + residuo)
 
 
numero = 12345
print(f"numero: {numero}, invertido: {invertir(numero, 0)}")