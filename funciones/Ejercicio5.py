#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
import math

def areaCirculo(radio):
    area=math.pi*radio**2
    return area
def volumenCilindro(radio, altura):
    volumen=math.pi*radio**2*altura
    return volumen

def decision(opcion):
    if opcion == 1:
        radio=float(input("Dime el radio del ciculo que quieres calcular: "))
        print("El area de tu circulo es de: ",areaCirculo(radio))
    if opcion == 2:
        radio=float(input("Dime el radio del cilindro: "))
        altura= float(input("Dime la altura del cilindro: "))
        return "El area del ciruculo es de ",areaCirculo(radio)
def programa():
    print("1. Calcular area del circulo.")
    print("2. Calcular el volumen de un cilindro")
    opcion=int(input("Que es lo que quieres calcular"))
    decision(opcion)
programa()