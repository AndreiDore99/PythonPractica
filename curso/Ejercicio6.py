n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))
n3 = int(input("Dime el tercer numero: "))

if n1>n2 and n1>n3:
    print("El numero mayor es el ",n1)
if n2>n3 and n2>n1:
    print("El numero mayor es el ",n2)
if n3>n1 and n3>n2:
    print("El numero mayor es el ",n3)