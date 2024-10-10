#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
#a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

opcion=input("Quieres que la pizza sea vegetaiana? Responde con s, si o n, no")
vegi=["pimiento","tofu"]
gordo=["peperoni","jamon","salmon"]
if opcion == "s":
    print(vegi)
    ing=int(input("Que otro ingrediente quieres? teclea el orden"))
    print("La pizza que se a pedido es de Mozarrella, tomate y ",vegi[ing-1])
else:
    print(gordo)
    ing=int(input("Que otro ingrediente quieres? teclea el orden"))
    print("La pizza que se a pedido es de Mozarrella, tomate y ",gordo[ing-1])