import os
import pandas as pd
import numpy as np
import shutil

def convert_to_yolo_format(df,
                           img_data_folder, 
                           output_folder):
    '''
    This function takes the data source path,the csv file convert it to a yolo format and output it to the out path.
    
    args: 
        
    
    '''
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, row in df.iterrows():
        filename = row['filename']
        img_path = os.path.join(img_data_folder, 
                                filename)
        label_path = os.path.join(output_folder, 
                                  filename.replace('.jpg', '.txt'))
        
        with open(label_path, 'w') as f:
            x_center = (row['xmin'] + row['xmax']) / 2 / row['width']
            y_center = (row['ymin'] + row['ymax']) / 2 / row['height']
            width = (row['xmax'] - row['xmin']) / row['width']
            height = (row['ymax'] - row['ymin']) / row['height']
            label = f"{row['class']} {x_center} {y_center} {width} {height}\n"
            f.write(label)

        shutil.copy(img_path, output_folder)

if __name__ == "__main__":
    train_df = pd.read_csv('data/train_labels.csv')
    test_df = pd.read_csv('data/test_labels.csv')

    convert_to_yolo_format(train_df, 'data/train', 'data/yolo_train')
    convert_to_yolo_format(test_df, 'data/test', 'data/yolo_test')
