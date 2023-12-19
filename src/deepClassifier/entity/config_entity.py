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


@dataclass(frozen=True)
class PrepareCallbackConfig:
    tensorboard_:Path
    model_path:Path


@dataclass(frozen=True)
class TrainerConfig:
    root_dir : Path
    trained_base_model_path : Path
    updated_base_model_path : Path
    params_epochs : int
    params_batch_size : int
    params_is_augmented : bool
    params_image_size : list


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model : Path
    training_data : Path
    image_size : list
    batch_size : int


