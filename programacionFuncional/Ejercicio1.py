def descuento(precio, descuento):
    return precio - precio * descuento / 100
def aniadir_iva(precio, iva):
    return precio + precio * iva /100
def precioLista(lista, funcion):
    total = 0
    for precio, descuento in lista.items():
        total+=funcion(precio,descuento)
    return total


print('El precio de la compra tras aplicar los descuentos es: ', precioLista({1000:20, 500:10, 100:1}, descuento))
print('El precio de la compra tras aplicar el IVA es: ', precioLista({1000:20, 500:10, 100:1}, aniadir_iva))