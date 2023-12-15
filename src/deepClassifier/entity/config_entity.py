from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    Source_URL:str
    local_data_file:Path
    unzip_dir:Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir:Path
    model_path:Path
    updated_model_path:Path
    params_image_size: list
    params_learning_rate : float
    params_include_top : bool
    params_weights : str
    params_classes: int