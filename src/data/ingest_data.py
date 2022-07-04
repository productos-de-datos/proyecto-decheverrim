"""
Data ingestion module from the external repository

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    
    import requests

    for num in range(1995, 2022):
        if num in range(2016, 2018):
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(num)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xls'.format(num), 'wb').write(file.content)
        else:
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(num)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xlsx'.format(num), 'wb').write(file.content)
    return
    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
