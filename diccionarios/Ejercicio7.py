cestaCompra={}
salir=True
while salir:
    articulo=input("Que es lo que vas a comprar?")
    precio=float(input("Cuanto vale?"))
    compra={articulo:precio}
    cestaCompra.update(compra)
    salir=input("Quieres agregar algo mas a la cesta de la compra? (S/N)") == "s"
precio= 0
for articulo in cestaCompra:
    precio+=cestaCompra[articulo]
print(cestaCompra," Y te vale toda la compra: ",precio)