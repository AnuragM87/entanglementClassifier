from fastapi import FastAPI
from backend.utils.quantum_utils import generate_random_two_qubit_state, is_entangled_ppt
from backend.data.features import compute_chsh_features
from fastapi import Body
from pydantic import BaseModel
from typing import List
from tensorflow import keras
import numpy as np
import os

app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'entanglement_classifier.h5')
model = keras.models.load_model(MODEL_PATH)

@app.get("/")
def read_root():
    return {"message": "Entanglement Classifier API is running."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

class StateFeatures(BaseModel):
    features: List[float]

@app.get("/generate-state")
def generate_state():
    rho = generate_random_two_qubit_state()
    label = int(is_entangled_ppt(rho))
    features = compute_chsh_features(rho)
    return {"features": features.tolist(), "label": label}

@app.post("/classify")
def classify_state(data: StateFeatures):
    features = np.array(data.features).reshape(1, -1)
    prob = model.predict(features)[0, 0]
    prediction = int(prob > 0.5)
    return {"prediction": prediction, "probability": float(prob)} 