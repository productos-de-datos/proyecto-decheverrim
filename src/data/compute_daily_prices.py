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

    
    Path_source = "./data_lake/cleansed/precios-horarios.csv"
    Data_cleansed = pd.read_csv(Path_source)
    Data_cleansed = Data_cleansed.groupby('fecha', as_index=False).mean()
    Data_cleansed = Data_cleansed[['fecha','precio']]
    Path_destiny = "./data_lake/business/precios-diarios.csv"
    Data_cleansed.to_csv(Path_destiny, index=False)
    print(Data_cleansed.head())


if __name__ == "__main__":
    import doctest
    compute_daily_prices()

    doctest.testmod()
