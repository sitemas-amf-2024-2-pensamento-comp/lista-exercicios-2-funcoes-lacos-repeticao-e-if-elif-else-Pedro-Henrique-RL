def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]

num = int(input("Digite um número inteiro positivo: "))
print("Os divisores de", num, "são:", divisores(num))
