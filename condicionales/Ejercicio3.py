#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Dime el dividendo: "))
divisor = int(input("Dime el divisor: "))
if divisor==0:
    print("Te crees gracioso?")
else:
    print(dividendo/divisor)