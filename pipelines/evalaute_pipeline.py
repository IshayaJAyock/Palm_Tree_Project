import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mlflow
from src.train_model import YOLOv8Model

data_path = 'data.yaml'
model_save_path = 'models/best_yolov8_model.pt'

# loading the  saved models
model = YOLOv8Model(model_save_path)

# Start MLflow run
with mlflow.start_run():
    model.evaluate(data_path=data_path)
    
    
