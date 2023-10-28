from typing import Optional

from pyspark.sql import SparkSession

from ds.core.model import ConfigModel
from ds.schema.order_payments import OrderPaymentsObject
from ds.spark_loader.base_loader import BaseLoader


class OrderPaymentsLoader(BaseLoader):
    def __init__(
        self, configs: ConfigModel, spark: Optional[SparkSession] = None
    ) -> None:
        """If spark is None, then just for local test."""
        self._spark = spark
        self._table_name = configs.source_tables.order_payments.view_name

    def load(self) -> OrderPaymentsObject:
        df = self._spark.read.table(self._table_name).toPandas()
        return OrderPaymentsObject(df)
