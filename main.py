from networksecurity.components.data_ingestion import dataingestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig
)
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.model_trainer import (ModelTrainerConfig,ModelTrainer
)

import sys
from networksecurity.components.data_ingestion import dataingestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataValidationConfig,DataTransformationConfig


try:
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(
        training_pipeline_config=training_pipeline_config
    )
    data_ingestion = dataingestion(
        data_ingestion_config=data_ingestion_config
    )
    logging.info("Initiate the data ingestion")
    dataingestionartifact = data_ingestion.initiate_data_ingestion()
    logging.info("Data Initiation completed")
    print(dataingestionartifact)
    
    data_validation_config = DataValidationConfig(training_pipeline_config)
    data_validation = DataValidation(dataingestionartifact,data_validation_config)       
    logging.info("Initiate Data Validation")
    data_validation_artifact = data_validation.initiate_data_validation()
    logging.info("Data Validation completed")
    print(data_validation_artifact)
    data_transformation_config = DataTransformationConfig(training_pipeline_config)
    logging.info("Data Transformation started")
    data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
    data_transformation_artifact = data_transformation.initiate_data_transformation()
    logging.info("Data Transformation completed")
    print(data_transformation_artifact)
    logging.info("Model Training stared")
    model_trainer_config=ModelTrainerConfig(training_pipeline_config)
    model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
    model_trainer_artifact=model_trainer.initiate_model_trainer()

    logging.info("Model Training artifact created")


except Exception as e:
    raise NetworkSecurityException(e,sys)
