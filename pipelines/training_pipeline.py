import os
import mlflow
from src.train_model import YOLOv8Model

data_path = 'data.yaml'
model_save_path = 'models/yolov8_finetuned.pt'

# Initialize YOLOv8 model
model = YOLOv8Model()

# Start MLflow run
with mlflow.start_run():
    
    # Finetuning the  model with custom data set
    model.fine_tune(data_path=data_path,
                    epochs=3, 
                    imgsz=640, 
                    device="mps", 
                    augment=True)
    
    # Log the trained model to MLflow
    mlflow.pytorch.log_model(model.model, 
                             "yolov8_finetuned.pt")
    
    # Save the model locally
    model.save_model(model_save_path)