import os
def create_data_lake():
    
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
    #Create the parent directory in the root of the proyect
    parent_directory = "data_lake"
    cwd = os.getcwd()
    path_parent_directory = os.path.join(cwd,parent_directory)
    
    #Remove if parent directory already exist
    if os.path.isdir(path_parent_directory):
        os.system("rm -rf " + path_parent_directory)
        os.mkdir(path_parent_directory)
    else:
        os.mkdir(path_parent_directory)
    
    #Create the directory's names
    directorys = ["landing","raw","cleansed","business"]
    directorys_business = ["business/reports","business/reports/figures","business/features","business/forecasts"]

    #Create the directorys
    for directory_name in directorys:
        os.mkdir(os.path.join(path_parent_directory, directory_name))

    for directory_name_business in directorys_business:
        os.mkdir(os.path.join(path_parent_directory, directory_name_business))


if __name__ == "__main__":
    import doctest

    create_data_lake()
    doctest.testmod()    



    
    #raise NotImplementedError("Implementar esta función")



