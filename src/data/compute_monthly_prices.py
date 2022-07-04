"""
Create a file with the average prices consolidated per month
"""

import pandas as pd
def compute_monthly_prices():
    """Compute los precios promedios mensuales.
    >>> compute_monthly_prices()
            fecha     precio
    0  1995-07-01   1.540655
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


    df_completed = pd.read_csv("./data_lake/cleansed/precios-horarios.csv")

    df_completed["year-month"] = df_completed["fecha"].map(lambda x: str(x)[0:7])

    df_completed = df_completed.groupby('year-month', as_index=False).mean()
    df_completed = df_completed[['year-month','precio']]
    df_completed = df_completed.rename(columns= {'year-month': 'fecha'})
    df_completed["fecha"] =  df_completed["fecha"].map(lambda x: x + str("-01"))
    route = "./data_lake/business/precios-mensuales.csv"
    df_completed.to_csv(route, index=False)
    print(df_completed.head())

if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
