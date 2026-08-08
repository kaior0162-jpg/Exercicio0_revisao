turno = str(input("Digite o seu turno?(M para Matutino, V para Verspertino ou N para Noturno)"))

if turno == "m":
    print("Bom Dia!")
elif turno == "v":
    print("Bom Tarde!")
elif turno == "n":
    print("Bom Noite!")
else :
    print("Valor Inválido!")