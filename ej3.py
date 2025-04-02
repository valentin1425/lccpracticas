def lucca(n):
    '''
    Diseño de datos:
    N = int
    signatura = int -> int
    Propósito:
    La sucesión luca
    Ejemplos:
    Lucca(0) = 2
    Lucca(1) = 1
    Lucca(2) = 3                
    '''
    if n == 0:
        return 2
    elif n  == 1:
        return n
    else :
        return lucca(n-1) + lucca (n-2)
    
def main():
    numero= (int(input ("ingrese un numero: ")))
    resultado = lucca(numero)
    print(resultado)


if __name__ == "__main__":
    main()

def lucca_test():
    assert lucca(0) == 2
    assert lucca(1) == 1
    assert lucca(2) == 3
    assert lucca(4) == 7     

