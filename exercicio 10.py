numeros = []
for _ in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

print("O maior número é:", max(numeros))
print("O menor número é:", min(numeros))
