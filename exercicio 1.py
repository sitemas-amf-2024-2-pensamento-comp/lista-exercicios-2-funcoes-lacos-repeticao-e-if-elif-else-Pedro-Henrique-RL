n = int(input("Digite um número inteiro positivo: "))

pares = []
impares = []

for i in range(1, n + 1):
    if i % 2 == 0:  
        pares.append(i)
    else:           
        impares.append(i)
    
print("Números pares:", pares)
print("Números ímpares:", impares)
