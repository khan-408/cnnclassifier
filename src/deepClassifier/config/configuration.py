from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directory
from deepClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig
from pathlib import Path

class ConfigurationManager:
    def __init__(self,
                config_file_path = CONFIG_FILE_PATH,
                params_file_path = PARAMS_FILE_PATH
                ):
        self.config = read_yaml(config_file_path)
        self.params= read_yaml(params_file_path)
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            Source_URL=config.Source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_prepare_base_model(self)->PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directory([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(root_dir=Path(config.root_dir),
                               model_path=Path(config.model_path),
                               updated_model_path=Path(config.updated_model_path),
                               params_image_size=self.params.IMAGE_SIZE,
                               params_learning_rate=self.params.LEARNING_RATE,
                               params_include_top=self.params.INCLUDE_TOP,
                               params_weights=self.params.WEIGHTS,
                               params_classes=self.params.CLASSES
        )
        return prepare_base_model_config
    
    def get_callbacks_config(self)-> PrepareCallbackConfig:


    
