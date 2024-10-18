asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturasSuspensas = []
for i in asignaturas:
    nota=float(input("Dime la nota de la asignatura "+i+": "))
    if nota < 5:
        asignaturasSuspensas.append(i)
print("Tienes que repetir : ",str(asignaturasSuspensas))