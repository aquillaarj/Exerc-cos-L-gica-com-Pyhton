horas = float(input("Digite o número de horas: "))
preco_kwh = float(input("Digite o preço por kwh: "))
consumo_kw = 0.35

custa= consumo_kw * preco_kwh * horas
print("O custo da impressão é: R$", custa)
