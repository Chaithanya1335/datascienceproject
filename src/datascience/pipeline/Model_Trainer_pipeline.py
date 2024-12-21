from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.Model_trainer import ModelTrainer
from src.datascience import logger

STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()
        