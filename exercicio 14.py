soma = 0
contador = 0
while True:
    nota = float(input("Digite uma nota (ou -1 para sair): "))
    if nota == -1:
        break
    soma += nota
    contador += 1

media = soma / contador if contador > 0 else 0
print("A média das notas é:", media)
