
def sumar_digitos(n):
    if(n==0):
        return 0
    else:
        return n % 10 + sumar_digitos(n//10)

n = int(input("Ingrese un número: "))
print(sumar_digitos(n))