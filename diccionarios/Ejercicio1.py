monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Dime una divisa:")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("No existe")