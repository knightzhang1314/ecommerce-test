from ds.core.platform import Platform
from ds.service.sales_service import SalesService

if __name__ == "__main__":
    platform = Platform()
    service = SalesService(platform)
    service.run()
