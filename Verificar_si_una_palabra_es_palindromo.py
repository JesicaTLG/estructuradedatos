
def palindromo(p):
    if p.lower() == p.lower()[::-1]:
        print('Tu palabra es un palindromo')
    else:
        print('No es un palindromo')
p = input('Ingresa una palabra: ')
palindromo(p)
