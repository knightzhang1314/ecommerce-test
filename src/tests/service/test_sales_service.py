from ds.core.platform import Platform
from ds.schema.order_items import OrderItemObject
from ds.schema.order_payments import OrderPaymentsObject
from ds.schema.orders import OrderObject
from ds.schema.product import ProductObject
from ds.schema.sales import SalesObject
from ds.service.sales_service import SalesService


def test_merge_sales(
    product: ProductObject,
    orders: OrderObject,
    order_items: OrderItemObject,
    order_payments: OrderPaymentsObject,
    sales: SalesObject,
) -> None:
    platform = Platform()
    service = SalesService(platform)
    sale_obj = service._merge_sales(
        orders.df, order_items.df, order_payments.df, product.df
    )
    assert sale_obj.df.equals(sales.df)
