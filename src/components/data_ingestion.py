import os
import sys
from src.exception import CustomException
import logging
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

    # given the input our class knows where to store the data

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        # in this variable we store the 3 other variables of where to store the data as soon as we call this class

    def initiate_data_ingestion(self):
        # here we read the data from the source
        logging.info("Entered the data ingestion method or coponent")
        try:
            # Read the data and logg the same
            df = pd.read_csv("notebooks\data\stud.csv")
            logging.info('Read the dataset as dataframe')

            # we now create the necessary folders whose path we stored in the ingestion_config and if the directory exists then no need to delete and recreate
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)

            # store the raw dataset at the given location / path
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            # perform train test split and then store them in their respective directories
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

