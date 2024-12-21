from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig,DatavalidationConfig,
                                                  DataTransformationconfig,ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_PATH,
                 schema_file_path=SCHEMA_PATH,
                 params_file_path=PARAMS_PATH ):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    def get_data_validation_config(self) -> DatavalidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DatavalidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_dir = config.unzip_dir,
            all_schema=schema,
        )

        return data_validation_config
    def get_data_transformation_config(self)->DataTransformationconfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationconfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config
    def get_model_trainer_config(self)->ModelTrainerConfig:
        config = self.config.model_trainer
        param = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])
        modelTrainerConfig = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=param.alpha,
            l1_ratio=param.l1_ratio,
            Target_column=  schema.name
        )
        return modelTrainerConfig


        