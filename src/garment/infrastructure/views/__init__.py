from garment.application.services.download_file_service import DownloadReadFileService
from garment.application.services.read_data_service import ReadDataService
from garment.infrastructure.repositories.mongo_product_repository import MongoGarmentRepository

garment_repository = MongoGarmentRepository()
download_read_file_service = DownloadReadFileService()
read_data_service = ReadDataService()
