

def fibonacci(n):
  if (n == 1):
    return(0)
  elif(n == 2):
    return(1)
  elif(n > 2):
    return(fibonacci(n - 1) + fibonacci(n - 2))


while True:
   n = int(input("Ingrese un número: "))
   if (n>=1):
       break
for i in range(n):
    print(fibonacci(i))




