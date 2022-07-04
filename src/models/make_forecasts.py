"""
Predict electricity prices according to days

"""

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pandas as pd
    import pickle
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import RandomForestRegressor

    daily_prices = pd.read_csv("data_lake/business/features/precios_diarios.csv", encoding = 'utf-8', sep=',')

    daily_prices["fecha"] = pd.to_datetime(daily_prices["fecha"]).dt.strftime('%Y%m%d')
    X_fecha = np.array(daily_prices['fecha']).reshape(-1,1)
    y_precio = np.array(daily_prices['precio']).reshape(-1,1)

    X_train, X_test, y_train, y_test = train_test_split(X_fecha, y_precio, test_size=0.3, random_state=123456,)

    clf = RandomForestRegressor(n_estimators=150, max_features='sqrt', n_jobs=-1, oob_score = True, random_state = 123456)

    clf.fit(X_train,y_train)
 
    pickled_model = pickle.load(open('src/models/precios_diarios.pickle', 'rb'))
    ypred=pickled_model.predict(X_test)

    X_test=pd.DataFrame(X_test, columns = ['fecha'])
    y_test=pd.DataFrame(y_test, columns = ['precio'])
    ypred=pd.DataFrame(ypred, columns = ['precio_pronostico'])

    forecasts_=pd.concat([X_test,y_test,ypred], axis=1)
    forecasts_.to_csv("data_lake/business/forecasts/precios_diarios.csv",index=None, header=True)

if __name__ == "__main__":
    import doctest
    make_forecasts()

    doctest.testmod()
