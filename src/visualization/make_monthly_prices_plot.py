"""
Create line graph that represents monthly average prices.

"""

def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_mes = pd.read_csv(r'data_lake/business/precios-mensuales.csv', sep=',', header=0, index_col=None)
    precios_mes['fecha'] = pd.to_datetime(precios_mes["fecha"])
    x = precios_mes.fecha
    y = precios_mes.precio
    plt.figure(figsize=(20, 10))
    plt.plot(x, y, 'g')
    plt.title('Promedio de Precios Mensuales')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation='vertical')
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()

    doctest.testmod()
    