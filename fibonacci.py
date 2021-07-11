# clase 3: Optimizacion Fibonacci

def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1
    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memo={}):
    if n ==0 or n==1:
        return 1

    try:
        return memo[n]
    
    except KeyError:
        resultado = fibonacci_dinamico(n-1,memo)+fibonacci_dinamico(n-2,memo)
        memo[n]=resultado

        return resultado

def fibonacci_series(n):
     
    # Taking 1st two fibonacci nubers as 0 and 1
    f = [0, 1]
     
     
    for i in range(2, n+1):
        #print(i)
        f.append(f[i-1] + f[i-2])
    return f[n]


if __name__ == '__main__':
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_series(n)
    print(resultado)