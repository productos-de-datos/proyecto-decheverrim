def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el file data_lake/cleansed/precios-horarios.csv.
    Las columnas de este file son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este file contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import glob
    import numpy as np

    Path = glob.glob(r'data_lake/raw/*.csv')

    list_=[]

    for file in Path : 
        df=pd.read_csv(file,index_col=None,header=0)
        list_.append(df)
    
    file_full=pd.concat(list_,axis=0,ignore_index=True)

    file_full=file_full[file_full["Fecha"].notnull()]
    file_full=pd.melt(file_full,id_vars=['Fecha'],var_name='hora', value_name='precio')
    file_full['hora']=np.where(pd.to_numeric(file_full['hora']) <= 9,pd.concat(["0"+file_full['hora']]),file_full['hora'])
    file_full["Fecha"] = pd.to_datetime(file_full["Fecha"]).dt.strftime('%Y-%m-%d')
    date1="2017-01-01"
    date2 = "2021-12-31"
    month_list = [i.strftime('%Y-%m-%d') for i in pd.date_range(start=date1, end=date2)]
    file_full=file_full[file_full.Fecha.isin(month_list)]
    file_full=file_full.rename(columns={"Fecha":"fecha"})
    file_full.to_csv("data_lake/cleansed/precios-horarios.csv",index=False, header=True)

    return

    raise NotImplementedError("Implementar esta función")




if __name__ == "__main__":
    import doctest
    clean_data()

    doctest.testmod()
