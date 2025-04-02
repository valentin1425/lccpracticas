def fibonacci(n):
    '''
    Diseño de datos:
    N: int > 0
    signatura:
    Fibonacci: int -> int
    Proposito:
    Hace la sucesión fibonacci.
    Ejemplos:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(2) = 1
    '''
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

def main():
    number = int(input("Ingrese un numero positivo: "))
    resultado = fibonacci(number)
    print(resultado)


if __name__ == "__main__":
    main()    


def fibonacci_test():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(8) == 21
    assert fibonacci(4) == 3