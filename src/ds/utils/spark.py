from typing import Dict, Optional

from pyspark.sql import SparkSession


def create_spark_session(spark_config: Optional[Dict] = None):
    spark_config = spark_config.get("spark_config", {}) if spark_config else {}
    spark_config["spark.sql.sources.partitionOverwriteMode"] = "dynamic"
    spark_config["hive.exec.dynamic.partition.mode"] = "nonstrict"
    spark_builder = SparkSession.builder.appName("spark")
    for k, v in spark_config.items():
        spark_builder.config(k, v)
    spark_session = spark_builder.enableHiveSupport().getOrCreate()
    return spark_session
