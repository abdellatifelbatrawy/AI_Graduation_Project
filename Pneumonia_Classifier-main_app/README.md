# 🫁 Pneumo Scan AI

> **Advanced Pneumonia Detection System using Deep Learning**

Pneumo Scan is a state-of-the-art web application designed to bridge the gap between artificial intelligence and radiology. It utilizes a Convolutional Neural Network (CNN) to analyze chest X-ray images, providing medical professionals with a rapid, accurate second opinion to aid in the early diagnosis of pneumonia.

## 📋 Table of Contents

* [About the Project](#about-the-project)
* [Key Features](#key-features)
* [Tech Stack](#tech-stack)
* [Installation & Setup](#installation--setup)
* [Usage](#usage)
* [The Team](#the-team)
* [Disclaimer](#disclaimer)

## 🧐 About the Project

Pneumonia is a life-threatening disease that requires early detection for effective treatment. Pneumo Scan allows users to upload digital X-ray scans and receive an analysis within seconds. The system classifies the image as either **"Normal"** or **"Pneumonia Detected"** and provides a confidence score to help interpret the results.

## ✨ Key Features

* **⚡ Rapid Analysis**: Get diagnostic results in under 2 seconds.
* **🧠 Deep Learning Powered**: Built on a custom-trained CNN model using TensorFlow/Keras.
* **🔒 Secure & Private**: Images are processed in real-time and are not permanently stored on the server.
* **📜 History Log**: A session-based history feature tracks all analyses performed during a single visit.
* **📱 Responsive Design**: Fully optimized for desktops, tablets, and mobile devices using Bootstrap 5.

## 🛠 Tech Stack

* **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
* **Backend**: Flask (Python)
* **AI/ML**: TensorFlow, Keras, OpenCV, NumPy

## 🚀 Installation & Setup

### Prerequisites

* Python 3.8 or higher
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pneumo-scan.git
cd pneumo-scan
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup the Model

Ensure your trained model file is named `model.h5` and placed in the root directory of the project.

> **Note:** The `model.h5` file is not included in the repository due to size limits. You must train the model or download it from the project resources.

### 5. Run the Application

```bash
python app.py
```

The application will start at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## 📖 Usage

1. Open the web interface in your browser.
2. Navigate to the **AI Detector** page.
3. Drag and drop a chest X-ray image (JPG, PNG) into the upload zone.
4. Click **Analyze Scan**.
5. View the result and confidence score immediately.
6. Check the **History** tab to review previous analyses.

## 👥 The Team

| Name                  | Contact                                                                     |
| --------------------- | --------------------------------------------------------------------------- |
| Ibrahim Hanafy        | [ibrahim.hanafy@zewailcity.edu.eg](mailto:ibrahim.hanafy@zewailcity.edu.eg) |
| Ali Elsayed           | [alimohammedelsayed05@gmail.com](mailto:alimohammedelsayed05@gmail.com)     |
| Omar Elbanna          | [Omar.essam10@msa.edu.eg](mailto:Omar.essam10@msa.edu.eg)                   |
| Ramez Mohamed         | [ramezm029@gmail.com](mailto:ramezm029@gmail.com)                           |
| Abdellatif El Batrawy | [abdellatifelbatrawy@gmail.com](mailto:abdellatifelbatrawy@gmail.com)       |
| Amr Ghoneim           | [Amrlghonim24@gmail.com](mailto:Amrlghonim24@gmail.com)                     |

## ⚠️ Disclaimer

This tool is for **educational and experimental purposes only**.
It is **not a substitute for professional medical advice, diagnosis, or treatment**.
Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
