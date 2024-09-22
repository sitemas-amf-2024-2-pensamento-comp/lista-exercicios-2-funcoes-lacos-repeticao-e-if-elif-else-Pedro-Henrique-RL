import random

numero_secreto = random.randint(1, 100)
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número entre 1 e 100: "))
    if tentativa < numero_secreto:
        print("Maior!")
    elif tentativa > numero_secreto:
        print("Menor!")
print("Parabéns! Você acertou o número:", numero_secreto)
