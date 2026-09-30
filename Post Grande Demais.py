LIMITE = 280

texto = input("Digite o texto do post: ")
tamanho = len(texto)

print(f"Seu post tem {tamanho} caracteres.")

if tamanho > LIMITE:
    excesso = tamanho - LIMITE
    print(f"Corte {excesso} caracteres")
else:
    print("Post dentro do limite.")