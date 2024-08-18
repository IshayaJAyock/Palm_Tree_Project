import torch
from PIL import Image
import io
import json
from ultralytics import YOLO

class ObjectDetectionModel:
    
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)

    def predict(self, image_bytes: bytes):
        image = Image.open(io.BytesIO(image_bytes))
        results = self.model(image)
        
        # This will extract the predictions
        predictions = []
        for result in results[0].boxes:
            predictions.append({
                'class': self.model.names[int(result.cls)],
                'confidence': float(result.conf),
                'bbox': result.xyxy.tolist()
            })
        
        return predictions