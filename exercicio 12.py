def multiplicacao_sucessiva(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("O resultado da multiplicação é:", multiplicacao_sucessiva(a, b))
