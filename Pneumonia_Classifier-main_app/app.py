from flask import Flask, render_template, request, redirect, url_for, flash
import os
import uuid
from datetime import datetime
# Assuming predict.py exists in the same directory as per your previous code
from predict import predict_image 

app = Flask(__name__)
app.secret_key = "secret_key_for_session" # Required for security if we expand later

# --- Configuration ---
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff'}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- IN-MEMORY STORAGE ---
HISTORY_LOG = []

# --- ROUTES ---

@app.route("/")
def home():
    """Landing Page"""
    return render_template("home.html")

@app.route("/about")
def about():
    """About Us and Team Page"""
    return render_template("about.html")

@app.route("/history")
def history():
    """Page to view past predictions"""
    return render_template("history.html", history=HISTORY_LOG)

@app.route("/detector", methods=["GET", "POST"])
def detector():
    """The X-Ray Prediction Page"""
    if request.method == "POST":
        if "image" not in request.files:
            return redirect(request.url)
        
        file = request.files["image"]

        if file.filename == "":
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Save file with unique name
            unique_filename = str(uuid.uuid4()) + "_" + file.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
            file.save(filepath)

            # Predict
            try:
                # Ensure predict_image is robust in your predict.py file
                label, probability = predict_image(filepath)
                
                # Log to History
                HISTORY_LOG.insert(0, {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "image": unique_filename,
                    "prediction": label,
                    "confidence": round(probability * 100, 2)
                })
                
            except Exception as e:
                return f"Error processing image: {e}"

            return render_template("detector.html", 
                                   prediction=label, 
                                   confidence=probability, 
                                   image_path=filepath)

    return render_template("detector.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)