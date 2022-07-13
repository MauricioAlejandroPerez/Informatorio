articulos = ["Mate", "Cafe", "Harina", "Palmitos", "Yerba", "Mermelada", "Cacao", "Picadillo"]
pedidos_por_articulo = {}
for articulo in articulos:
    pedidos_por_articulo[articulo] = 0

for articulo in pedidos_por_articulo:
    print(articulo, pedidos_por_articulo[articulo])