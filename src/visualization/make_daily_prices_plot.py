def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    Dialy_prices = pd.read_csv("./data_lake/business/precios-diarios.csv")
    plt.plot(Dialy_prices["fecha"], Dialy_prices["precio"])
    plt.savefig('./data_lake/business/reports/figures/daily_prices.png')



if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()

    doctest.testmod()
