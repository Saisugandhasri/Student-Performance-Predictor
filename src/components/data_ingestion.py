import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig: #to declare paths
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion: # This class will handle everything related to reading, splitting, and saving data.
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() ## When the class is initialized, it sets up your config object (self.ingestion_config)


    def initiate_data_ingestion(self):  # This is the function that does the entire ingestion process — reading the CSV, splitting it, saving it.

        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # #✔️ Saves the raw original dataset into artifacts/data.csv , index=False: avoids saving DataFrame index column, header=True: includes column names

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

# train_test_split(df) → 2 outputs

# train_test_split(X, y) → 4 outputs

# train_test_split(X, y, z) → 6 outputs (and so on…)
                                       
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            # Saves the split train and test sets to:

            # artifacts/train.csv

            # artifacts/test.csv


            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            ) # Returns the two saved file paths so other parts of the pipeline (like transformation/training) can use them. 
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
#  Calls the next step in the ML pipeline: data transformation.

# Passes the train/test CSVs to transform them into arrays suitable for training a model.



    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



