#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e
#imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en
#cuenta mayúsculas y minúsculas.

contrasena = "pepE"
passwd=input("Dime la contraseña: ")
if passwd.upper()==contrasena.upper():
    print("Correcto")
else:
    print("Pero que dices chaval")