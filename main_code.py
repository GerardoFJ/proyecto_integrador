import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

def publicaciones(data):
    list_years = data["Year"].tolist()
    list_y = []
    for i in list_years:
        if i not in list_y:
            try:
                list_y.append(int(i))
            except:
                list_y = list_y
    list_count =[]
    for i in list_y:
        list_count.append(list_years.count(i))

    fig, ax = plt.subplots()

    ax.bar(list_y, list_count)

    ax.set_ylabel('AÑOS')
    ax.set_title('Publicaciones por año')
    ax.legend(title='Publicaciones por año')

    plt.show()




def main():
    data = pd.
    data = pd.read_csv("vgsales.csv")
    publicaciones(data)


if __name__ == "__main__":
    main()
