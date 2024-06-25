"""
Calcul du factoriel
"""

# fonction recursive
def factorial(n: int):
    if n < 0:
        raise ValueError("Le paramètre n doit être supérieur ou égal à zéro")
    if n == 0:
        return 1
    return n * factorial(n-1)

# function tail recursive
def factorial_tr(nombre: int):
    def factorial_local(n: int, accumulator: int):
        if n == 0:
            return accumulator
        return factorial_local(n-1, n * accumulator)
    
    if nombre < 0:
        raise ValueError("Le paramètre n doit être supérieur ou égal à zéro")
    return factorial_local(nombre, 1)

"""
Calcul de Fibonacci
"""

# fonction recursive
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Le paramètre n doit être supérieur ou égal à zéro")
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# function tail recursive
def fibonacci_tr(n: int) -> int:
    def fibonacci_local(terme: int, prec: int, prec_2: int) -> int:
        if terme == n:
            return prec + prec_2
        return fibonacci_local(terme+1, prec + prec_2, prec)
    
    if n < 0:
        raise ValueError("Le paramètre n doit être supérieur ou égal à zéro")
    if n < 2:
        return n
    return fibonacci_local(2,1,0)


if __name__ == "__main__":
    # print(factorial(7))
    # print(factorial_tr(7))

    print(fibonacci(10))
    print(fibonacci_tr(10))
