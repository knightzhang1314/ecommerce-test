from pydantic import BaseModel, Field


class TableInfo(BaseModel):
    view_name: str = Field(default=None, description="the table name.")
    url: str = Field(default=None, description="the data url.")
    type: str = Field(default=None, description="the platform which exists the data.")
    partition: str = Field(default=None, description="the partition of the table.")


class SourceTableInfo(BaseModel):
    products: TableInfo
    order_items: TableInfo
    order_payments: TableInfo
    orders: TableInfo


class TargetTableInfo(BaseModel):
    sales: TableInfo


class ConfigModel(BaseModel):
    country_name: str = Field(default="")
    source_tables: SourceTableInfo
    target_tables: TargetTableInfo
