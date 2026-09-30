nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("media: ", round(media, 2))

if media >= 6.0:
  print("Aprovado")
else:
  print("Recuperação")