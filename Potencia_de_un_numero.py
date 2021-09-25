def potencia(a,b):
    if (b==0):
        return 1
    elif(a==0):
        return 0
    elif(b==1):
        return a
    else:
        return a *potencia(a,b -1)

a = int(input("Ingrese un número: "))
b = int(input("Ingrese la potencia: "))
print(potencia(a,b))
