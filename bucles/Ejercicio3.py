numero = int(input("Dime un numero: "))
print("Los numeros impares hasta llegar al numero indicado son : ")

for i in range (numero):
    if i%2==0:
        print(i+1,end=", ")