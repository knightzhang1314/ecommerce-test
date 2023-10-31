from typing import Optional

import pandas as pd
from pyspark.sql import SparkSession

from ds.core.model import ConfigModel
from ds.schema.product import ProductObject
from ds.spark_loader.base_loader import BaseLoader


class ProductLoader(BaseLoader):
    def __init__(
        self, configs: ConfigModel, spark: Optional[SparkSession] = None
    ) -> None:
        """If spark is None, then just for local test."""
        self._spark = spark
        self._table_name = configs.source_tables.products.view_name
        self._url = configs.root_path.joinpath(configs.source_tables.products.url)
        self._type = configs.source_tables.products.type

    def load(self) -> ProductObject:
        df = (
            self._spark.read.table(self._table_name).toPandas()
            if self._type != "local"
            else pd.read_csv(self._url)
        )
        return ProductObject(df)
