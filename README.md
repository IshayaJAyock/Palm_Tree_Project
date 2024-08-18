# PalmTreeProject
 
This project fine-tunes the YOLOv8 model on custom object detection data. It is designed with a modular approach, Dockerized, and integrates MLOps tools like DVC and MLflow for experiment tracking.

## Project Structure
- `data/`: Contains raw and processed data.
- `src/`: Contains the core code for data loading, model training, and evaluation.
- `src/models/`: Contains the YOLOv8 model implementation.
- `src/utils/`: Contains utility functions for data processing and model evaluation.
- `pipelines/`: Containes codes on ingestion, preparation,training and evaluation pipelines
- `docker/`: Docker and Docker Compose files for containerization.
- `mlflow/`: MLflow configuration files.
- `tests/`: Unit tests for the model and utility functions.
- `requirements.txt`: Python dependencies.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/IshayaJAyock/PalmTreeProject.git
   cd PalmTreeProject
   ```

2. Build the Docker image and start the container:
    ```bash 
    docker-compose up --build
    ``` 
3. Track experiments with MLflow:
    ```bash
    docker-compose up mlflow
    ```
4. Training the Model
    ```bash 
    python src/train.py
    ``` 

5. Evaluate the model
    ```bash
    python src/evaluate.py
    ``` 

