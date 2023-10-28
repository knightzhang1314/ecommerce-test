from ds.core.platform import Platform


def test_platform_config():
    platform = Platform("US")
    assert set(platform.configs.source_tables.dict().keys()) == {
        "products",
        "order_items",
        "order_payments",
        "orders",
    }
    assert set(platform.configs.target_tables.dict().keys()) == {"sales"}
    assert platform.configs.country_name == "US"
