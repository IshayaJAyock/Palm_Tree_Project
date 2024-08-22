import os
import sys
from pathlib import Path



# ingest data from kaggle
class IngestDataFromKaggle:
    
    def __init__(self, kaggle_username, 
                 kaggle_key, 
                 competition_name):
        
        self.kaggle_username = kaggle_username
        self.kaggle_key = kaggle_key
        self.competition_name = competition_name
        self.kaggle_api_token = self._get_kaggle_api_token()
        self.kaggle_competition_id = self._get_kaggle_competition_id()
        self.kaggle_dataset_id = self._get_kaggle_dataset_id()
        self.kaggle_data_path = self._get_kaggle_data_path()
    
    def ingest(self):
        # download data from kaggle
        self._download_data_from_kaggle()
        # extract data from zip file
        self._extract_data_from_zip_file()
        # move data to data directory
        self._move_data_to_data_directory()
        
        
        


        