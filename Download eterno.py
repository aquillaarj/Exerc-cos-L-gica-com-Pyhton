mb = float(input("Tamanho do arquivo em mb: "))
mbps = float(input("velocidade da internet em mbps: "))

tempo = mb * 8 / mbps 
print("Download em", tempo, "segundos")
