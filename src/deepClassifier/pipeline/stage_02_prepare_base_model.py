from deepClassifier.components.stage_02_preparation import PrepareBaseModel
from deepClassifier.config.configuration import ConfigurationManager
from deepClassifier import logger

STAGE_NAME = 'Prepare Base Model'

def main():

    config =ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model()
    prepared_model = PrepareBaseModel(config=prepare_base_model_config)
    prepared_model.get_base_model()
    prepared_model.update_base_model()


if __name__=='__main__':
    try:
        logger.info(f'**************************')
        logger.info(f'>>>>>>>>>_Stage {STAGE_NAME} Started.')
        main()
        logger.info(f'>>>>>>>>>_Stage {STAGE_NAME} Completed.')

    except Exception as e:
        logger.exception(e)
        raise e
