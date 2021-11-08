from product.application.services.download_file_service import DownloadReadFileService
from product.application.services.read_data_service import ReadDataService
from product.infrastructure.repositories.mongo_product_repository import MongoProductRepository

product_repository = MongoProductRepository()
download_read_file_service = DownloadReadFileService()
read_data_service = ReadDataService()
