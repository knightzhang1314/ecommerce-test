from typing import Optional

import pandas as pd
from pyspark.sql import SparkSession

from ds.core.model import ConfigModel
from ds.schema.orders import OrderObject
from ds.spark_loader.base_loader import BaseLoader


class OrdersLoader(BaseLoader):
    def __init__(
        self, configs: ConfigModel, spark: Optional[SparkSession] = None
    ) -> None:
        """If spark is None, then just for local test."""
        self._spark = spark
        self._table_name = configs.source_tables.orders.view_name
        self._url = configs.root_path.joinpath(configs.source_tables.orders.url)
        self._type = configs.source_tables.orders.type

    def load(self) -> OrderObject:
        df = (
            self._spark.read.table(self._table_name).toPandas()
            if self._type != "local"
            else pd.read_csv(self._url)
        )
        return OrderObject(df)
