from functools import reduce

import pandas as pd

from ds.core.platform import Platform
from ds.schema.sales import SalesObject
from ds.service.base_service import BaseService
from ds.spark_loader.order_items_loader import OrderItemsLoader
from ds.spark_loader.order_loader import OrdersLoader
from ds.spark_loader.order_payments_loader import OrderPaymentsLoader
from ds.spark_loader.product_loader import ProductLoader
from ds.spark_writer.spark_writer import SparkWriter
from ds.utils.spark import create_spark_session


class SalesService(BaseService):
    def __init__(self, platform: Platform):
        self.configs = platform.configs

    def run(self) -> None:
        configs = self.configs
        spark = create_spark_session()
        order = OrdersLoader(configs, spark).load().df
        order_items = OrderItemsLoader(configs, spark).load().df
        order_payments = OrderPaymentsLoader(configs, spark).load().df
        product = ProductLoader(configs, spark).load().df
        sales = self._merge_sales(order, order_items, order_payments, product).df
        SparkWriter(spark, sales, configs).write()

    def _merge_sales(
        self,
        order: pd.DataFrame,
        order_items: pd.DataFrame,
        order_payments: pd.DataFrame,
        product: pd.DataFrame,
    ) -> SalesObject:
        dfs = [order, order_items, order_payments]
        orders = reduce(lambda left, right: pd.merge(left, right, on="order_id"), dfs)
        sales = pd.merge(orders, product, on="product_id")
        return SalesObject(sales)
