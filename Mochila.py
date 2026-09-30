peso_m = float(input("Digite o peso da mochilinha!: "))
peso_p= float(input("Digite o seu peso, imensa: ")) 

porcentagem = (peso_m / peso_p) * 100

print(f"A mochilinha pesa {porcentagem:.2f}% do seu peso.")

if peso_m > peso_p * 0.10:
    print("A mochilinha é pesada demais pra vc seu frangote!")   

else:
    print("A mochilinha é leve, vamo pra iskola!")