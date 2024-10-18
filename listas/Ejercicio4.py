numeroGanador= []
for i in range(6):
    numeroGanador.append(int(input("Dime un numero ganador:")))
numeroGanador.sort()
print(str(numeroGanador))