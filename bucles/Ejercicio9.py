passwd = "andreidore"

while True:
    palabra = input("Dime la contraseña: ")
    if palabra==passwd:
        print("Correcto")
        break
    else:
        print("Incorrecto")