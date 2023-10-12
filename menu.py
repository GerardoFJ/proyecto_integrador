from main_code import publicaciones(data), global_sales_genre(data), global_sales_publisher(data), genero_year(data), videojuegos_genero(data), north_america_sales_year(data),  japan_sales_year(data), other_sales_year(data), top_3_genero(data)
def menu():
    print("⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒ Hola!⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒\n")
    print("Selecciona una de las opciones dadas")
    print("1. Videojuegos publicados con respecto a los años")
    print("2. Ventas globales con respecto al género ")
    print("3. Ventas globales con respecto a la compañia")
    print("4. Género con respecto al año de lanzamiento")
    print("5. Cantidad de videojuegos por género")
    print("6. Ventas en NorteAmerica con respecto a los años")
    print("7. Ventas en Japon con respecto a los años")
    print("8. Ventas de otros con respecto a los años")
    print("9. Top 3 de videojuegos mas populares por género")
    print("10. Compañia que genera mayores ventas")
    print("11. Área con mayor derrame económico")
    print("12. % que aporta cada área a las ventas globales")

    diccionario = {
        1: publicaciones(data),
        2: global_sales_genre(data),
        3: global_sales_publisher(data),
        4: genero_year(data),
        5: videojuegos_genero(data),
        6: north_america_sales_year(data),
        7: japan_sales_year(data),
        8: other_sales_year(data),
        9: top_3_genero(data),
        10:  ,
        11: from main_code import ,
        12: from main_code import , 
    }

def main():
    respuesta = "si"
    while respuesta =="si":
        menu()
        switch
