from pathlib import Path

import pandas as pd
import pytest

from ds.schema.order_items import OrderItemObject
from ds.schema.order_payments import OrderPaymentsObject
from ds.schema.orders import OrderObject
from ds.schema.product import ProductObject
from ds.schema.sales import SalesObject


@pytest.fixture
def source_path() -> Path:
    source_path = Path(__file__).resolve().parent.parent.joinpath("source")
    return source_path


@pytest.fixture
def product(source_path: Path) -> ProductObject:
    fp = source_path.joinpath("olist_products_dataset.csv")
    df = pd.read_csv(fp)
    return ProductObject(df)


@pytest.fixture
def orders(source_path: Path) -> OrderObject:
    fp = source_path.joinpath("olist_orders_dataset.csv")
    df = pd.read_csv(fp)
    return OrderObject(df)


@pytest.fixture
def order_items(source_path: Path) -> OrderItemObject:
    fp = source_path.joinpath("olist_order_items_dataset.csv")
    df = pd.read_csv(fp)
    return OrderItemObject(df)


@pytest.fixture
def order_payments(source_path: Path) -> OrderPaymentsObject:
    fp = source_path.joinpath("olist_order_payments_dataset.csv")
    df = pd.read_csv(fp)
    return OrderPaymentsObject(df)


@pytest.fixture
def sales(source_path: Path) -> SalesObject:
    fp = source_path.joinpath("olist_sales_dataset.csv")
    df = pd.read_csv(fp)
    return SalesObject(df)
