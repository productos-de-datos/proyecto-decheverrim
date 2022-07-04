def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd
    
    for year in range(1995, 2022):        
        if year in range(1995, 2000):
            csv_data = pd.read_excel('data_lake/landing/{}.xlsx'.format(year), header=3)
            csv_data = csv_data.iloc[:, 0:25]
            csv_data.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']       
            csv_data.to_csv('data_lake/raw/{}.csv'.format(year),index=None)
        elif year in range(2000, 2016):
            csv_data = pd.read_excel('data_lake/landing/{}.xlsx'.format(year), header=2)
            csv_data = csv_data.iloc[:, 0:25]
            csv_data.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            csv_data.to_csv('data_lake/raw/{}.csv'.format(year),index=None)
        elif year in range(2016, 2018):
            csv_data = pd.read_excel('data_lake/landing/{}.xls'.format(year), header=2)
            csv_data = csv_data.iloc[:, 0:25]
            csv_data.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            csv_data.to_csv('data_lake/raw/{}.csv'.format(year), index=None)
        else:
            csv_data = pd.read_excel('data_lake/landing/{}.xlsx'.format(year), header=0)
            csv_data = csv_data.iloc[:, 0:25]
            csv_data.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            csv_data.to_csv('data_lake/raw/{}.csv'.format(year), index=None)
    return
    raise NotImplementedError("Implementar esta función")
    


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
