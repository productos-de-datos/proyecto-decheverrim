def compute_daily_prices():
    """Compute los precios promedios diarios.
    >>> compute_daily_prices()
            fecha    precio
    0  1995-07-20  1.409435
    1  1995-07-21  4.924333
    2  1995-07-22  1.269500
    3  1995-07-23  0.953083
    4  1995-07-24  4.305917

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    import pandas as pd

    Price_Schedule_Cleansed = pd.read_csv("data_lake/cleansed/precios-horarios.csv",index_col=None,header=0)
    Price_Schedule_Cleansed =  Price_Schedule_Cleansed[["fecha", "precio"]]
    Dialy_prices = Price_Schedule_Cleansed.groupby("fecha").mean({"precio"})
    Price_Schedule_Cleansed.to_csv("data_lake/business/precios-diarios.csv",index=None, header=True)
    
    print(Price_Schedule_Cleansed.head())
    return


    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    compute_daily_prices()

    doctest.testmod()
