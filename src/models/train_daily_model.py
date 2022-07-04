"""
Train the model for forecasting

"""

import pandas as pd
import pickle

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

def train_daily_model():
    """
    
    Entrena el modelo de pronóstico de precios diarios.
    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl

    """

    df = pd.read_csv("data_lake/business/features/precios_diarios.csv", encoding = 'utf-8', sep=',')

    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y%m%d')
    X_fecha = np.array(df['fecha']).reshape(-1,1)
    y_precio = np.array(df['precio']).reshape(-1,1)

    X_train, X_test, y_train, y_test = train_test_split(X_fecha, y_precio, test_size=0.3, random_state=123456)


    clf = RandomForestRegressor(n_estimators=150, max_features='sqrt', n_jobs=-1, oob_score = True, random_state = 123456)
    
    clf.fit(X_train,y_train)

    pickle.dump(clf, open('src/models/precios-diarios.pkl',"wb"))


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()