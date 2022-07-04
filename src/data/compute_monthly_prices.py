def compute_monthly_prices():
    """Compute los precios promedios mensuales.
    >>> compute_monthly_prices()
            fecha     precio
    0  1995-07-01   1.540199
    1  1995-08-01   7.086462
    2  1995-09-01  10.955819
    3  1995-10-01  10.445442
    4  1995-11-01  27.534782

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd

    Path_source = "./data_lake/cleansed/precios-horarios.csv"
    Data_cleansed = pd.read_csv(Path_source)
    Data_cleansed["year-month"] = Data_cleansed["fecha"].map(lambda x: str(x)[0:7])
    Data_cleansed = Data_cleansed.groupby('year-month', as_index=False).mean()
    Data_cleansed = Data_cleansed[['year-month','precio']]
    Data_cleansed = Data_cleansed.rename(columns= {'year-month': 'fecha'})
    Data_cleansed["fecha"] =  Data_cleansed["fecha"].map(lambda x: x + str("-01"))
    Path_destiny = "./data_lake/business/precios-mensuales.csv"
    Data_cleansed.to_csv(Path_destiny, index=False)
    print(Data_cleansed.head())
    


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
