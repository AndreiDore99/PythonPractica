nombre=input("Cual es tu nombre?")
edad=input("Cuantos años tienes?")
direccion=input("En donde vives?")
num=input("Dime tu numerod de telefono: ")
persona={'nombre':nombre,'edad':edad,'direccion':direccion,'numeroTelf':num}
print(persona['nombre']," tiene ",persona["edad"]," años y vive en ",persona["direccion"]," y su telefono de contacto es el: ",persona["numeroTelf"])