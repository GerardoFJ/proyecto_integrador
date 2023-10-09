import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

def separador(lista_init):
    lista_fin = []
    for i in lista_init:
        if i not in lista_fin:
            lista_fin.append(i)
    return lista_fin



def publicaciones(data):
    list_years = data["Year"].tolist()
    list_y = []
    
    list_count =[]
    for i in list_y:
        list_count.append(list_years.count(i))

    fig, ax = plt.subplots()

    ax.bar(list_y, list_count)

    ax.set_ylabel('AÑOS')
    ax.set_title('Publicaciones por año')
    ax.legend(title='Publicaciones por año')

    plt.show()

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
    plt.bar(list_plataform, list_sales)
    plt.xticks(rotation=90)
    plt.show()
    
    
def salesNA_by_year(data):
    ventas = data["NA_Sales"].tolist()
    años = data["Year"].tolist()
    list_years = separador(años)
    list_sales = [0 for i in range(len(list_years))]

    for i in range(len(ventas)):
        list_sales[list_years.index(años[i])] += ventas[i]

    print (list_years)
    print (list_sales)
    print (len(list_years))
    print (len(list_sales))
    plt.bar(list_years, list_sales)
    plt.xticks(rotation=90)
    plt.show()


    


def main():
    data = pd.read_csv("vgsales.csv")
    #publicaciones(data)
    #global_sales(data)
    salesNA_by_year(data)


if __name__ == "__main__":
    main()
