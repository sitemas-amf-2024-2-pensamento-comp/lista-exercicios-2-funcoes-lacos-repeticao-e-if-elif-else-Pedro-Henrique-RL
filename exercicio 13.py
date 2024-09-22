def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Tabela de Conversão de Celsius para Fahrenheit:")
for c in range(0, 101, 10):
    f = celsius_para_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")
