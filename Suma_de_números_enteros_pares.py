lis=[1,6,8,10,13,22,4]
def sumapares(lista):
    if len(lista) ==0:
        return 0
    elif lista[0] % 2==0:
        return lista[0] + sumapares(lista[1:])
    else:
        return sumapares(lista[1:])
print(sumapares(lis))
