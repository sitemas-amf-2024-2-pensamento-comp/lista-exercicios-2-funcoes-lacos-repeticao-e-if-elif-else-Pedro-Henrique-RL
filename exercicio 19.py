def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for char in texto if char in vogais)

frase = input("Digite uma frase: ")
print("Número de vogais na frase:", contar_vogais(frase))
