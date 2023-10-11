import pandas as pd
import matplotlib.pyplot as plt

#FUNCION MENU PARA MOSTRAR LAS OPCIONES EN LA CONSOLA
def menu():
    print("********************************************BIENVENIDO********************************************") 
    print("""Elige una opcion que quieras conocer por medio de una grafica:""")
    print("1. Graficar la cantidad de videojuegos publicados con respecto al Año de Lanzamiento")
    print("2. Graficar las Ventas Globales con respecto a la Compañía de videojuegos")
    print("3. Graficar las Ventas de NorteAmérica con respecto al año")
    print("4. Graficar el Género del videojuego con respecto a los Años de lanzamiento")
    print("5. Determinar el top 3 de videojuegos más populares de cada género")
    print("Otro numero para salir")
    num = int(input("Ingresa el numero de la opcion que deseas: "))
    return num


#FUNCION PARA SEPARAR EN 1 SOLO ELEMENTO LOS DATOS REPETIDOS
def separador(lista_init):
    lista_fin = []
    for i in lista_init:
        try:
            if (int(i)) not in lista_fin:
                lista_fin.append(str(int(i)))
        except:
            pass
    return lista_fin


#Graficar la cantidad de videojuegos publicados con respecto al Año de Lanzamiento
def publicaciones(data):
    list_years = data["Year"].tolist()
    list_only_one_year = separador(list_years)
    list_only_one_year.sort()
    list_count = [0 for i in range(len(list_only_one_year))]
    for i in list_years:
        try:
            list_count[list_only_one_year.index(str(int(i)))] += 1
        except:
            pass
    plt.bar(list_only_one_year, list_count)
    plt.title("Cantidad de videojuegos publicados segun el año")
    plt.xlabel("Año de Lanzamiento")
    plt.ylabel("Cantidad de videojuegos publicados")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()



#Graficar la cantidad de videojuegos publicados con respecto al Año de Lanzamiento    
def globalsales_x_genre(data):
    genero = data["Genre"].tolist()
    global_sales = data["Global_Sales"].tolist()
    
    list_generos = separador(genero)
    if 1989 in list_generos:
        list_generos.remove(1989)

    list_sales = [0 for i in range(len(list_generos))]

    for i in range(len(global_sales)):
        list_sales[list_generos.index(genero[i])] += global_sales[i]
    
    
    plt.plot(list_generos, list_sales)
    plt.xticks(rotation=90)
    plt.show()

#Graficar el Género del videojuego con respecto a los Años de lanzamiento
def genero_x_year(data):
    genero = data["Genre"].tolist()
    años = data["Year"].tolist()
    list_generos = separador(genero)
    list_years = separador(años)
    list_count = [0 for i in range(len(list_generos))]

    for i in range(len(genero)):
        list_count[list_generos.index(genero[i])] += 1

    
    plt.bar(list_generos, list_count)
    plt.xticks(rotation=90)
    plt.show()  



#Graficar las Ventas Globales con respecto a la Compañía de videojuegos
def global_sales(data):
    ventas = data["Global_Sales"].tolist()
    company = data["Platform"].tolist()
    list_plataform = separador(company)
    list_sales = separador(ventas)
    
    for i in range(len(ventas)):
        if i < len(list_plataform):
            list_sales[list_plataform.index(company[i])] += ventas[i]

    plt.stem(list_plataform, list_sales)
    plt.xticks(rotation=90)
    plt.show()
    
# Graficar las Ventas de NorteAmérica con respecto al año  
def salesNA_by_year(data):
    ventas = data["NA_Sales"].tolist()
    años = data["Year"].tolist()
    list_years = separador(años)
    list_years.sort()
    list_sales = [0 for i in range(len(list_years))]
    
    for i in range(len(ventas)):
        try:
            list_sales[list_years.index(str(int(años[i])))] += round(ventas[i],2)
        except:
            list_sales[list_years.index(str(años[i]))] += round(ventas[i],2)
    

   
    plt.stackplot(list_years, list_sales)
    plt.xticks(rotation=90)
    plt.show()

#Determinar el top 3 de videojuegos más populares de cada género
def top_x_genero(data):
    generos = data["Genre"].tolist()
    videojuegos = data["Name"].tolist()
    list_generos = separador(generos)

    

#Main Function
def main():
    data = pd.read_csv("vgsales.csv")
    publicaciones(data)
    respuesta = "si"
    data = pd.read_csv("vgsales.csv")
    while respuesta.lower() in ("si", "si","si","si"):
        num = menu()
        if num == 1:
            publicaciones(data)
        elif num == 2:
            global_sales(data)
        elif num == 3:
            salesNA_by_year(data)
        elif num == 4:
            globalsales_x_genre(data)
        elif num == 5:
            genero_x_year(data)
        else:
            print("Gracias por usar el programa")
            break
        print("Desea volver al menu principal?")
        respuesta = input( "Si/No: ").lower()

if __name__ == "__main__":
    main()
