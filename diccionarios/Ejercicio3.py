frutas={'platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
fruta= input("Que frta es la que quieres?").title()
peso=float(input("Cuantos kg has cogudo?"))
if fruta in frutas:
    print(peso," KG, a ",frutas[fruta]," valen ",frutas[fruta]*peso)
else:
    print("No exixte tu fruta en mi inventario, chorry")