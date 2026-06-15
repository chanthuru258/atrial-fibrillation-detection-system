# ❤️ Atrial Fibrillation Detection System Using Deep Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10-orange)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-red)

---

## 📌 Project Overview

This project detects **Atrial Fibrillation (AF)** from ECG signals using
**Convolutional Neural Networks (CNN)** with a Django web interface.

The system allows users to upload `.npy` ECG signal files and get instant
predictions whether the signal is **Normal** or **Abnormal (AF)**.

---

## 👨‍💻 Team Members

| Name |
|------|
| Mr. Antony Jawan J |
| Mr. Chanthuru S |
| Mr. Gopala Krishnan C |
| Mr. Guru Prakash B |

**Guide:** Mrs. S. Femila Sweetly, M.E., Assistant Professor

---

## 🏫 Institution

**SBM College of Engineering & Technology, Dindigul - 624005**
**Anna University, Chennai - 600025**
**April 2026**

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, Bootstrap 5
- **Backend:** Python, Django
- **Deep Learning:** TensorFlow, Keras (CNN Model)
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib
- **Image Processing:** OpenCV

---

## 📁 Project Structure

```
atrial_fibrillation_detection/
│
├── static/
│   └── PLACE_MODEL_HERE.txt   ← Trained CNN Model
│
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                          ← Uploads Model
│   ├── urls.py
│   └── views.py                           ← Main Logic
│
├── atrial_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── index.html                         ← Web Interface
│
├── requirements.txt
├── README.md
└── manage.py
```

---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/chanthuru258/atrial-fibrillation-detection-system.git
cd atrial-fibrillation-detection
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Start the Server
```bash
python manage.py runserver
```

### Step 5: Open Browser
```
http://127.0.0.1:8000
```

---

## 🔬 How It Works

1. User uploads a `.npy` ECG signal file
2. Django backend receives and saves the file
3. CNN model loads and analyzes the ECG signal
4. Signal is reshaped and passed to the model
5. Model predicts: **Normal** or **Abnormal (AF)**
6. ECG graph is plotted and displayed to the user

---

## 🧠 CNN Model Architecture

```
Input Layer
    ↓
Convolutional Layer (Feature Extraction)
    ↓
ReLU Activation
    ↓
Max Pooling Layer
    ↓
Convolutional Layer
    ↓
Max Pooling Layer
    ↓
Fully Connected Layer
    ↓
Softmax Output Layer
    ↓
Output: Normal / Abnormal
```

---

## 📊 Results

| Metric | Value |
|--------|-------|
| The CNN model successfully classified ECG signals into Normal and Atrial Fibrillation categories during testing.

## 🔮 Future Work

- Integrate with smartwatches for real-time monitoring
- Mobile application development
- Cloud-based storage for remote doctor access
- Detect other arrhythmias beyond AF
- Larger dataset training for better accuracy

---

## 📚 References

1. Rajpurkar et al. (2017) - Deep Learning for Arrhythmia Detection
2. PhysioNet MIT/BIH Atrial Fibrillation Database
3. Bhavnani et al. (2016) - Mobile Technology in Healthcare
