import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pathlib import Path
from src.moveTextFiles import MoveTextFiles
from src.prepare_data import PrepareData
import pandas as pd
import numpy as np





def preprpcessData(df, data_path ,
                   output_path):
    df = pd.read_csv(df)    
    process = PrepareData(df,
                          data_path, 
                          output_path)
    process.convert_to_yolo_format(df,
                                   data_path, 
                                   output_path)


if __name__ == "__main__":
    
    
    data_path =  "data/raw_data"
    train_data_path = data_path +  "/train"
    test_data_path = data_path + "/test"
    
    train_df = data_path + "/train_labels.csv" 
    test_df = data_path + "/train_labels.csv"
   
    data_path2 = "data"
    train_output_path = data_path2 + "/palmdata/train/images"
    test_output_path = data_path2 + "/palmdata/test/images"
    
    train_preproces = preprpcessData(train_df, 
                                     train_data_path, 
                                     train_output_path)
    test_preproces = preprpcessData(test_df, 
                                    test_data_path, 
                                    test_output_path) 
    
    # Moving ..txt files to seperate folders
    
    # From training text files
    
    source_folder = train_output_path
    destination_folder = data_path + "/palmdata/train/labels"
    move_train_labels = MoveTextFiles(source_folder,
                                      destination_folder)
    move_train_labels.move_txt_files()
    
    # For testing text files
    source_folder = test_output_path
    destination_folder = data_path + "/palmdata/test/labels"
    move_test_labels = MoveTextFiles(source_folder, 
                                     destination_folder)
    move_test_labels.move_txt_files()
    