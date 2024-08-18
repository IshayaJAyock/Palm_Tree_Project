import sys
import torch
from ultralytics import YOLO


class YOLOv8Model:
    
    def __init__(self, 
                 model_path=None):
        self.model = YOLO('pre_train_models/yolov8n.pt') if model_path is None else YOLO(model_path)

    def fine_tune(self, data_path,  
                  epochs=10, 
                  imgsz=640, 
                  device="mps" 
                  ,augment=True):
        
        self.model.train(data=data_path, 
                         epochs=epochs, 
                         imgsz=imgsz, 
                         device=device, 
                         augment=augment)

    def evaluate(self, 
                 data_path):
        
        return self.model.val(data=data_path)

    def save_model(self, 
                   path):
        
        self.model.save(path) 