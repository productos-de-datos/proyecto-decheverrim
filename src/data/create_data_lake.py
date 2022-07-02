from multiprocessing import parent_process


def create_data_lake():
    import os
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
 
    """
    #Create data lake
    os.mkdir("data_lake")
    parent_directory = "data_lake"

    #Delete if data_lake already exist
    cwd = os.getcwd()
    path_data_lake = os.path.join(cwd, parent_directory)
    if os.path.isdir(path_data_lake):
        os.system("rm -rf "+ parent_directory)
    
    #Create directory
    directorys = ["landing","raw","cleansed","business"]
    directorys_business = ["business/reports","business/reports/figures","business/features","business/forecasts"]
    for directory in directorys:
        os.mkdir(os.path.join("data_lake",directory))
    for directory_business in directorys_business:
        os.mkdir(os.path.join("data_lake",directory_business))
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    create_data_lake()
