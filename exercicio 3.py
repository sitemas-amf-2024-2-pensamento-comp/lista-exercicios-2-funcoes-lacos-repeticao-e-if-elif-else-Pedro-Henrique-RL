a = int(input("Digite o primeiro número inteiro positivo (a): "))
b = int(input("Digite o segundo número inteiro positivo (b): "))

soma = 0

if a > b:
    a, b = b, a  


for i in range(a, b + 1):
    if i % 3 == 0:  
        soma += i   


print("A soma dos números entre", a, "e", b, "que são divisíveis por 3 é:", soma)
