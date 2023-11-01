from functools import reduce
from typing import Optional

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
    def __init__(self, platform: Optional[Platform] = None):
        self.configs = platform.configs if platform else Platform().configs

    def run(self) -> SalesObject:
        configs = self.configs
        spark = create_spark_session()
        order = OrdersLoader(configs, spark).load().df
        order_items = OrderItemsLoader(configs, spark).load().df
        order_payments = OrderPaymentsLoader(configs, spark).load().df
        product = ProductLoader(configs, spark).load().df
        sales = self._merge_sales(order, order_items, order_payments, product)
        group_sales = self._group_sales(sales)
        SparkWriter(spark, group_sales, configs).write()
        return SalesObject(sales)

    def _merge_sales(
        self,
        order: pd.DataFrame,
        order_items: pd.DataFrame,
        order_payments: pd.DataFrame,
        product: pd.DataFrame,
    ) -> pd.DataFrame:
        dfs = [order, order_items, order_payments]
        orders = reduce(lambda left, right: pd.merge(left, right, on="order_id"), dfs)
        sales = pd.merge(orders, product, on="product_id")
        return sales

    def _group_sales(self, sales: pd.DataFrame) -> pd.DataFrame:
        df = sales[["order_purchase_timestamp", "product_id", "payment_value"]]

        # group sales by product and week
        df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
        df = df.set_index("order_purchase_timestamp")
        grouped_sales = df.groupby(["product_id", pd.Grouper(freq="W")]).sum()
        grouped_sales = grouped_sales.reset_index()
        return grouped_sales


class LocalSalesService(SalesService):
    def __init__(self, platform: Optional[Platform] = None):
        super().__init__(platform)
        self.configs = platform.configs if platform else Platform().configs

    def run(self) -> SalesObject:
        configs = self.configs
        order = OrdersLoader(configs).load().df
        order_items = OrderItemsLoader(configs).load().df
        order_payments = OrderPaymentsLoader(configs).load().df
        product = ProductLoader(configs).load().df
        sales = self._merge_sales(order, order_items, order_payments, product)
        group_sales = self._group_sales(sales)
        group_sales = group_sales.rename(columns={"payment_value": "sales"})
        return SalesObject(group_sales)
