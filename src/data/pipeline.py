"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""

import luigi
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_daily_prices import compute_daily_prices
from compute_monthly_prices import compute_monthly_prices

class IngestData(luigi.Task):
    """
    Run the task to retrieve data from an external file
    """
    def output(self):
        return []

    def run(self):
        ingest_data()

class TransformData(luigi.Task):
    """
    Executes the task of transforming the data and consolidating it into a single file
    """
    def output(self):
        return []

    def run(self):
        transform_data()

class CleanData(luigi.Task):
    """
    Executes the task to clean the data
    """
    def output(self):
        return []

    def run(self):
        clean_data()

class ComputeDailyPrices(luigi.Task):
    """
    Executes the task of consolidating prices daily

    """
    def output(self):
        return []

    def run(self):
        compute_daily_prices()

class ComputeMonthlyPrices(luigi.Task):
    """
    Executes the task of consolidating prices monthly
    """
    def output(self):
        return []

    def run(self):
        compute_monthly_prices()


def pipeline():
    """
    Call pipeline
    """
    luigi.build([IngestData(), TransformData(), CleanData(), ComputeDailyPrices(), ComputeMonthlyPrices() ],  local_scheduler=True)


if __name__ == "__main__":
    import doctest
    pipeline()
    doctest.testmod()
