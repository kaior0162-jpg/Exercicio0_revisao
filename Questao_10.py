mt = int(input("Montar a tabuada de: "))
cm = int(input("Começar por: "))
tm = int(input("Terminar em: "))

tmr = tm + 1

for i in range(cm, tmr, 1):

    print(f"{mt} x {i} = {mt*i}")