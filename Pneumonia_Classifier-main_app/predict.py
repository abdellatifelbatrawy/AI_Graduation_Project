import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import sigmoid

# --- Load Model Once (Global Scope) ---
MODEL_PATH = "model.h5"

if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH, compile=False)
    print("Model loaded successfully.")
else:
    print(f"Error: {MODEL_PATH} not found. Please place it in the project directory.")
    model = None

IMG_SIZE = 320 

def predict_image(image_path, threshold=0.15):
    if model is None:
        return "Model Error", 0.0

    # --- Preprocess Image ---
    try:
        img = cv2.imread(image_path)
        if img is None:
            return "Error: Image not found", 0.0
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
    except Exception as e:
        return f"Image Error: {str(e)}", 0.0

    # --- Predict ---
    logits = model.predict(img)[0][0]
    prob = sigmoid(logits).numpy()

    # --- Confidence Calculation ---
    if prob >= threshold:
        # High probability of Pneumonia -> High confidence in "Pneumonia"
        return "Pneumonia Detected", float(prob)
    else:
        # Low probability of Pneumonia -> High confidence in "Normal"
        # Example: prob is 0.04 (4%), so Confidence is 0.96 (96%)
        return "Normal", float(1 - prob)