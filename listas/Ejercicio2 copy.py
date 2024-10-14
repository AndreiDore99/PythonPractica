asignaturas = ["Mate","Fisica","Lengua","Historia","Religion"]
notas = []
for i in range (0,len(asignaturas)):
    notas[i]=input("Que nota has sacado en ",asignaturas[i],":")
    notas.append(notas)

print("Has sacado las siguientes notas entonces: ")
for i in range (0, len(asignaturas)):
    print("En ",asignaturas[i]," has sacado :",notas[i])