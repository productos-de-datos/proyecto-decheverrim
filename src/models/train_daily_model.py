def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    import numpy as np
    import pickle
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import ElasticNet
    from sklearn.model_selection import GridSearchCV
 
    df = pd.read_csv("data_lake/business/features/precios_diarios.csv", sep=",")
    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y%m%d')
    y = df["precio"]
    x = df.copy()
    x.pop("precio")

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=123456)

    estimator = GridSearchCV(
        estimator=ElasticNet(
            random_state=12345,
        ),
        param_grid={
            "alpha": np.linspace(0.05, 0.5, 10),
            "l1_ratio": np.linspace(0.05, 0.5, 10),
        },
        cv=5,
        refit=True,
        verbose=1,
        return_train_score=False,
    )
    estimator.fit(x_train,y_train)
    estimator =estimator.best_estimator_

    with open("proyecto-decheverrim/src/models/precios_diarios.pickle","wb") as file:
        estimator = pickle.dump(estimator,file)







if __name__ == "__main__":
    import doctest
    train_daily_model()

    doctest.testmod()
