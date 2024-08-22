import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mlflow
from src.train_model import YOLOv8Model

data_path = 'data.yaml'
model_save_path = 'models/yolov8_finetuned.pt'

# Initialize YOLOv8 model
model = YOLOv8Model()


# Finetuning the  model with custom data set
model.fine_tune(data_path=data_path,
                epochs=100, 
                imgsz=640, 
                device="mps", 
                augment=True)

# Save the model locally
model.save_model(model_save_path)