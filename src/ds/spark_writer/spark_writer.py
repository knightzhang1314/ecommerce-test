import pandas as pd
from pyspark.sql import SparkSession

from ds.core.model import ConfigModel
from ds.spark_writer.base_writer import BaseWriter


class SparkWriter(BaseWriter):
    def __init__(self, spark: SparkSession, df: pd.DataFrame, config: ConfigModel):
        self._spark = spark
        self._df = df
        self._target_table = config.target_tables.sales.view_name
        self._partition = config.target_tables.sales.partition

    def write(self) -> None:
        df = self._spark.createDataFrame(self._df)
        writer = df.write.mode("overwrite").format("parquet")
        if self._partition:
            writer = writer.partitionBy(self._partition)
        writer.saveAsTable(self._target_table)
