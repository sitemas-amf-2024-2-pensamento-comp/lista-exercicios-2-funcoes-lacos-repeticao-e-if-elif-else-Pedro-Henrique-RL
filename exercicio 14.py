valor_emprestimo = float(input("Digite o valor do empréstimo: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
meses = int(input("Digite o número de meses para pagar: "))
salario = float(input("Digite seu salário: "))

prestacao_mensal = valor_emprestimo * (taxa_juros * (1 + taxa_juros) ** meses) / ((1 + taxa_juros) ** meses - 1)

if prestacao_mensal > salario * 0.30:
    print("Empréstimo negado. A prestação mensal é maior que 30% do seu salário.")
else:
    print("Empréstimo aprovado! A prestação mensal é:", prestacao_mensal)
