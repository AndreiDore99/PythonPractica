#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

nHoras = float(input("Cuantas horas haces por dia?"))
costoHoras= float(input("A cuanto te pagan la hora?"))
print("Al dia deberias de estar cobrando ",(costoHoras*nHoras))