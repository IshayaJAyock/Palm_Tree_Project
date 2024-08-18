import cv2
import numpy as np
from flask import Flask, request, jsonify
from src.model_loader import ObjectDetectionModel
from ultralytics import YOLO



app = Flask(__name__)

# Initializing the model
model = ObjectDetectionModel('models/best_yolov8_model.pt')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()

    predictions = model.predict(image_bytes)

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)