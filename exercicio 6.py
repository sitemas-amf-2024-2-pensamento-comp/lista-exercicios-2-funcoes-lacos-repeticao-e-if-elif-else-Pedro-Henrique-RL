def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Digite um número inteiro: "))
print("Os primeiros números da sequência de Fibonacci são:", fibonacci(n))
