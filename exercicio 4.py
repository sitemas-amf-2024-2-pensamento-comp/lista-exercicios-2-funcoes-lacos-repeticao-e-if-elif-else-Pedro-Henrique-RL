n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    fatorial = 1
    i = 1

    while i <= n:
        fatorial *= i
        i += 1

    print(f"O fatorial de {n} é {fatorial}")
