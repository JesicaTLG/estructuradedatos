

def sumaDigitos(num):
    s=num
    while num>0:
        s+s+num%10
        num=num//10
    return s

n=int(input("cantidad de numeros: "))
sumat=0
while n>0:
    num=int(input("numero: "))
    sumat= sumat + sumaDigitos(num)
    n=n-1
print(sumat)