
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.Model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evauation_config()
        model_evaluation= ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()