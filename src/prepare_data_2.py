import os
import pandas as pd
import numpy as np
import shutil



class PrepareData:
    def __init__(self, dataframe,
                 data_path, 
                 output_path):
        
        self.df = dataframe
        self.img_data_path = data_path
        self.output_path = output_path
    
    def convert_to_yolo_format(self):
        '''
        This function takes the data source path,the csv file convert it to a yolo format and output it to the out path.
        args: 
        '''
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        for index, row in self.df.iterrows():
            
            self.filename = row['filename']
            self.img_path = os.path.join(self.img_data_path, 
                                    self.filename)
            self.label_path = os.path.join(self.output_path, 
                                    self.filename.replace('.jpg', '.txt'))
            
            with open(self.label_path, 'w') as f:
                self.x_center = (row['xmin'] + row['xmax']) / 2 / row['width']
                self.y_center = (row['ymin'] + row['ymax']) / 2 / row['height']
                self.width = (row['xmax'] - row['xmin']) / row['width']
                self.height = (row['ymax'] - row['ymin']) / row['height']
                self.label = f"{row['class']} {self.x_center} {self.y_center} {self.width} {self.height}\n"
                f.write(self.label)

            shutil.copy(self.img_path, self.output_path)