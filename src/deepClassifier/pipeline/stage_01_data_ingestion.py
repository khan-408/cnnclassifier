from deepClassifier.components.stage_01_data_ingestion import DataIngestion
from deepClassifier.config.configuration import DataIngestionManager
from deepClassifier import logger

config = DataIngestionManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(config=data_ingestion_config)