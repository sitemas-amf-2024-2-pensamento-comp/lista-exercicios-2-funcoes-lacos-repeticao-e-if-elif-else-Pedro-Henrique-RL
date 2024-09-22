def soma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

num = int(input("Digite um número inteiro positivo: "))
print("A soma dos dígitos é:", soma_digitos(num))
