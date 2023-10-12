import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#FUNCION MENU PARA MOSTRAR LAS OPCIONES EN LA CONSOLA

#FUNCION PARA SEPARAR EN 1 SOLO ELEMENTO LOS DATOS REPETIDOS
def separador(lista_init):
    lista_fin = []
    for i in lista_init:
        try:
            if (str(int(i))) not in lista_fin:
                lista_fin.append(str(int(i)))
        except:
            if (str(i)) not in lista_fin:
                lista_fin.append(str(i))

    return lista_fin

#FUNCION PARA ORDENAR 2 LISTAS DE MAYOR A MENOR SEGUN LA SEGUNDA LISTA
def sorter_double(lista1, lista2):
    lista_3 = [x for _,x in sorted(zip(lista2,lista1),reverse=True)]
    lista2.sort(reverse=True)
    return lista_3, lista2


#Graficar la cantidad de videojuegos publicados con respecto al Año de Lanzamiento
def publicaciones(data):
    list_years = data["Year"].tolist()
    list_only_one_year = separador(list_years)
    list_only_one_year.sort()
    list_only_one_year.remove("nan")
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

#Graficar las Ventas Globales con respecto al Género del videojuegos
def global_sales_genre(data):
    genero = data["Genre"].tolist()
    global_sales = data["Global_Sales"].tolist()
    list_genero = separador(genero)
    list_count = [0 for i in range(len(list_genero))]

    for i in range(len(genero)):
        list_count[list_genero.index(str(genero[i]))] += round(global_sales[i],2)
    
    list_count = [round(i,2) for i in list_count]
    
    print(list_genero)
    print(list_count)

    plt.bar(list_genero, list_count)
    plt.title("Ventas globales segun el género del videojuego")
    plt.xlabel("Género del videojuego")
    plt.ylabel("Ventas globales en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

#Graficar las Ventas Globales con respecto a la Compañía de videojuego
def global_sales_publisher(data):
    publicadores = data["Publisher"].tolist()
    global_sales = data["Global_Sales"].tolist()
    list_publicadores = separador(publicadores)
    list_count = [0 for i in range(len(list_publicadores))]

    for i in range(len(publicadores)):
        list_count[list_publicadores.index(str(publicadores[i]))] += round(global_sales[i],2)
    
    list_count = [round(i,2) for i in list_count]
    
    list_publicadores, list_count = sorter_double(list_publicadores, list_count)
    
    plt.bar(list_publicadores, list_count)
    plt.title("Ventas globales de cada compañia")
    plt.xlabel("Compañias")
    plt.ylabel("Ventas globales en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()
#   
#Graficar el Género del videojuego con respecto a los Años de lanzamiento
def genero_year(data):
    genero = data["Genre"].tolist()
    years = data["Year"].tolist()
    list_years = separador(years)
    list_years.remove("nan")
    list_years.sort()
    list_count=[]
    for j in list_years:
        list_micro_count = []
        for i in range(len(genero)):
            try:
                comp = str(int(years[i]))
            except:
                comp = str(years[i])
            if comp == j:
                if genero[i] not in list_micro_count:
                    list_micro_count.append(genero[i])

        list_count.append(len(list_micro_count))

    plt.bar(list_years, list_count)
    plt.title("Cantidad de generos de videojuegos publicados segun el año")
    plt.xlabel("Año de Lanzamiento")
    plt.ylabel("Cantidad de generos de videojuegos publicados")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

#Graficar la cantidad de videojuegos que hay por Género
def videojuegos_genero(data):
    genero = data["Genre"].tolist()
    list_genero = separador(genero)
    list_count = [0 for i in range(len(list_genero))]

    for i in range(len(genero)):
        list_count[list_genero.index(str(genero[i]))] += 1
    

    plt.bar(list_genero, list_count)
    plt.title("Cantidad de videojuegos por género")
    plt.xlabel("Género del videojuego")
    plt.ylabel("Cantidad de videojuegos")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

#Graficar las Ventas de NorteAmérica con respecto al año 
def north_america_sales_year(data):
    years = data["Year"].tolist()
    north_america_sales = data["NA_Sales"].tolist()
    list_years = separador(years)
    list_years.remove("nan")
    list_years.sort()
    list_count = [0 for i in range(len(list_years))]

    for i in range(len(years)):
        try:
            list_count[list_years.index(str(int(years[i])))] += round(north_america_sales[i],2)
        except:
            pass
    
    list_count = [round(i,2) for i in list_count]
    
    plt.bar(list_years, list_count)
    plt.title("Ventas de NorteAmérica segun el año")
    plt.xlabel("Año de Lanzamiento")
    plt.ylabel("Ventas de NorteAmérica en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

#Graficar las Ventas Japón con respecto al año
def japan_sales_year(data):
    years = data["Year"].tolist()
    japan_sales = data["JP_Sales"].tolist()
    list_years = separador(years)
    list_years.remove("nan")
    list_years.sort()
    list_count = [0 for i in range(len(list_years))]

    for i in range(len(years)):
        try:
            list_count[list_years.index(str(int(years[i])))] += round(japan_sales[i],2)
        except:
            pass
    
    list_count = [round(i,2) for i in list_count]
    
    plt.bar(list_years, list_count)
    plt.title("Ventas de Japón segun el año")
    plt.xlabel("Año de Lanzamiento")
    plt.ylabel("Ventas de Japón en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

#Graficar las Ventas Otros con respecto al año
def other_sales_year(data):
    years = data["Year"].tolist()
    other_sales = data["Other_Sales"].tolist()
    list_years = separador(years)
    list_years.remove("nan")
    list_years.sort()
    list_count = [0 for i in range(len(list_years))]

    for i in range(len(years)):
        try:
            list_count[list_years.index(str(int(years[i])))] += round(other_sales[i],2)
        except:
            pass
    
    list_count = [round(i,2) for i in list_count]
    
    plt.bar(list_years, list_count)
    plt.title("Ventas de Otros segun el año")
    plt.xlabel("Año de Lanzamiento")
    plt.ylabel("Ventas de Otros en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

#Determinar el top 3 de videojuegos más populares de cada género.
def top_3_genero(data):
    genero = data["Genre"].tolist()
    videojuego = data["Name"].tolist()
    global_sales = data["Global_Sales"].tolist()
    gen_new = separador(genero)
    list_top3 = [[] for i in gen_new]
    
    for i in range(len(global_sales)):
        if len(list_top3[gen_new.index(genero[i])]) != 3:
            list_top3[gen_new.index(genero[i])].append([videojuego[i], global_sales[i]])

    list_x = []
    list_y = []
    option = 0
    for i in list_top3[option]:
        list_x.append(i[0])
        list_y.append(i[1])
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d} millones)"
    wedges, texts, autotexts = ax.pie(list_y, autopct=lambda pct: func(pct, list_y),
                                    textprops=dict(color="w"))
    ax.legend(wedges, list_x,
            title="Videojuegos",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title(f"Top 3 de videojuegos más populares de {gen_new[option]}")
    plt.show()

#Determinar qué compañía genera mayores ventas.
def top_companies(data):
    publicadores = data["Publisher"].tolist()
    global_sales = data["Global_Sales"].tolist()
    list_publicadores = separador(publicadores)
    list_count = [0 for i in range(len(list_publicadores))]

    for i in range(len(publicadores)):
        list_count[list_publicadores.index(str(publicadores[i]))] += round(global_sales[i],2)
    
    list_count = [round(i,2) for i in list_count]
    
    list_publicadores, list_count = sorter_double(list_publicadores, list_count)
    print(len(list_publicadores))
    list_publicadores  = list_publicadores[:10]
    list_count = list_count[:10]
    
    plt.bar(list_publicadores, list_count)
    plt.title("Top 10 compañias con mas ventas")
    plt.xlabel("Compañias")
    plt.ylabel("Ventas globales en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()
    
#. Determinar qué área geográfica tiene mayor derrame económico en comparación al resto.
def graphic_area(data):
    na_sales = data["NA_Sales"].tolist()
    eu_sales = data["EU_Sales"].tolist()
    jp_sales = data["JP_Sales"].tolist()
    other_sales = data["Other_Sales"].tolist()
    list_types = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    list_sales = [sum(na_sales), sum(eu_sales), sum(jp_sales), sum(other_sales)]
    
    list_types, list_sales = sorter_double(list_types, list_sales)
   
    plt.bar(list_types, list_sales)
    plt.title("Ventas de cada zona")
    plt.xlabel("Compañias")
    plt.ylabel("Ventas en Millones")
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()

    


def main():
    data = pd.read_csv("vgsales.csv")
    


if __name__ == "__main__":
    main()
