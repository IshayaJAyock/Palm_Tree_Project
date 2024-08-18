import os
import sys
from pathlib import Path
from src.ingest_data import IngestDataFromKaggle

def ingestingData(your_kaggle_username, your_kaggle_key, your_competition_name):
    
        # Creating a new instance of the IngestDataFromKaggle class
        ingest_data = IngestDataFromKaggle(kaggle_username,
                                           kaggle_key,
                                           competition_name)
        ingest_data.ingest()
    
    
if __name__ == '__main__':
    kaggle_username = 'your_kaggle_username'
    kaggle_key = 'your_kaggle_key'
    competition_name = 'your_competition_name'
    ingestingData(kaggle_username, kaggle_key, competition_name)
    
    