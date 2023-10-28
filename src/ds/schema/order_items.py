import pandas as pd
import pandera as pa
from pandera import dtypes
from pandera.typing import Series

from ds.schema.base_schema import BaseObject


class OrderItemObject(BaseObject):
    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__(df)
        self._df = pd.DataFrame(OrderItemSchema.validate(df))

    @property
    def df(self) -> pd.DataFrame:
        return self._df.copy()


class OrderItemSchema(pa.DataFrameModel):
    order_id: Series[dtypes.String] = pa.Field(nullable=False)
    product_id: Series[dtypes.String] = pa.Field(nullable=True)

    class Config:
        strict = False
        coerce = True
