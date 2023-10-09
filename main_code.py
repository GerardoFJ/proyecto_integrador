import pandas as pd
import matplotlib.pyplot as plt

def menu():
    ///////////////BIENVENIDO/////////////////////
    """Elige una opcion para graficar los datos de los videojuegos"""
    num= int(input())
    if num == 1:
    print("1. Graficar la cantidad de videojuegos publicados con respecto al Año de Lanzamiento")

    print("2. Graficar las Ventas Globales con respecto a la Compañía de videojuegos")
    print("3. Graficar las Ventas de NorteAmérica con respecto al año")
    print("4. Graficar el Género del videojuego con respecto a los Años de lanzamiento")
    print("5. Determinar el top 3 de videojuegos más populares de cada género")
    print("6. Salir")
    





def separador(lista_init):
    lista_fin = []
    for i in lista_init:
        try:
            if str(int(i)) not in lista_fin:
                lista_fin.append(str(int(i)))
        except:
            if str(i) not in lista_fin:
                lista_fin.append(str(i))

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
            list_count[list_only_one_year.index(str(i))] += 1
    
    
    #print(list_only_one_year)
    #print(list_count)

    
    plt.bar(list_only_one_year, list_count)
    plt.xticks(rotation=90)
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
    
    print(list_generos)
    print(list_sales)
    print (len(list_generos))
    print (len(list_sales))
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

    print(list_generos)
    print(list_count)
    print (len(list_generos))
    print (len(list_count))
    plt.bar(list_generos, list_count)
    plt.xticks(rotation=90)
    plt.show()  



#Graficar las Ventas Globales con respecto a la Compañía de videojuegos
def global_sales(data):
    ventas = data["Global_Sales"].tolist()
    company = data["Platform"].tolist()
    list_plataform = separador(company)

    list_sales = [0 for i in range(len(list_plataform))]
    
    for i in range(len(ventas)):
        list_sales[list_plataform.index(company[i])] += ventas[i]
    
    print(list_plataform)
    print(list_sales)
    print (len(list_plataform))
    print (len(list_sales))
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
    print(list_years)
    
    for i in range(len(ventas)):
        try:
            list_sales[list_years.index(str(int(años[i])))] += round(ventas[i],2)
        except:
            list_sales[list_years.index(str(años[i]))] += round(ventas[i],2)
    

    print (list_years)
    print (list_sales)
    print (len(list_years))
    print (len(list_sales))
    
    plt.stackplot(list_years, list_sales)
    plt.xticks(rotation=90)
    plt.show()

#Determinar el top 3 de videojuegos más populares de cada género
def top_x_genero(data):
    generos = data["Genre"].tolist()
    videojuegos = data["Name"].tolist()
    list_generos = separador(generos)

    


def main():
    data = pd.read_csv("vgsales.csv")
    #publicaciones(data)
    #global_sales(data)
    #salesNA_by_year(data)
    globalsales_x_genre(data)
    #genero_x_year(data)

if __name__ == "__main__":
    main()
