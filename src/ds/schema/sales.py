import pandas as pd
import pandera as pa
from pandera import dtypes
from pandera.typing import Series

from ds.schema.base_schema import BaseObject, BaseSchema


class SalesObject(BaseObject):
    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__(df)
        self._df = pd.DataFrame(SalesSchema.validate(df))

    @property
    def df(self) -> pd.DataFrame:
        return self._df.copy()


class SalesSchema(BaseSchema):
    order_id: Series[dtypes.String] = pa.Field(nullable=False)
    product_id: Series[dtypes.String] = pa.Field(nullable=True)
    product_category_name: Series[dtypes.String] = pa.Field(nullable=True)
    payment_value: Series[dtypes.Float32] = pa.Field(nullable=True)
    order_purchase_timestamp: Series[dtypes.Timestamp] = pa.Field(nullable=True)

    class Config:
        strict = False
        coerce = True
