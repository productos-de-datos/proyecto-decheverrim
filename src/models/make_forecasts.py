"""
Predict electricity prices according to days

"""
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.
    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:
    * La fecha.
    * El precio promedio real de la electricidad.
    * El pronóstico del precio promedio real.
    """
    

    # Lea el archivo `precios-diarios` y asignelo al DataFrame `df`
    df = pd.read_csv("data_lake/business/features/precios_diarios.csv", encoding = 'utf-8', sep=',')

    # Asigne a la variable los valores de la columna `fecha`
    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y%m%d')
    X_fecha = np.array(df['fecha']).reshape(-1,1)

    # Asigne a la variable los valores de la columna `precio`
    y_precio = np.array(df['precio']).reshape(-1,1)

    # Divida los datos de entrenamiento y prueba. La semilla del generador de números
    # aleatorios es 123456. El tamaño de la muestra de entrenamiento es del 80%
    (X_train, X_test, y_train, y_test,) = train_test_split(X_fecha, y_precio, test_size=0.3, random_state=123456,)

    # Cree una instancia del modelo de regresión lineal
    clf = RandomForestRegressor(n_estimators=150, max_features='sqrt', n_jobs=-1, oob_score = True, random_state = 123456)
    
    # Entrene el clasificador usando X_train y y_train
    clf.fit(X_train,y_train)

    #Realiza el Forecast 
    pickled_model = pickle.load(open('src/models/precios-diarios.pickle', 'rb'))
    ypred=pickled_model.predict(X_test)

    X_test=pd.DataFrame(X_test, columns = ['fecha'])
    y_test=pd.DataFrame(y_test, columns = ['precio'])
    ypred=pd.DataFrame(ypred, columns = ['precio_pronostico'])

    dtfinal=pd.concat([X_test,y_test,ypred], axis=1)
    dtfinal.to_csv("data_lake/business/forecasts/precios-diarios.csv",index=None, header=True)


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
