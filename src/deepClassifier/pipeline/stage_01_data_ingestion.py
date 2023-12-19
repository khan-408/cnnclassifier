from deepClassifier.components.stage_01_data_ingestion import DataIngestion
from deepClassifier.config.configuration import ConfigurationManager
from deepClassifier import logger

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(config=data_ingestion_config)