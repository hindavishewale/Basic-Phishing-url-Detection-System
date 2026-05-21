# 🔐 PhishGuard — Basic Phishing URL Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5-orange)
![Status](https://img.shields.io/badge/Status-Educational-yellow)

> **⚠️ Disclaimer:** This is a basic educational project built for learning purposes.
> It is NOT intended for production security use or real-world threat detection.
> Always use professional security tools for actual cybersecurity needs.

---

## 📌 Project Overview

PhishGuard is a beginner-level machine learning project that detects whether a given
URL is **Phishing** or **Legitimate** using feature extraction and classification algorithms.

It demonstrates the intersection of **Cybersecurity** and **Machine Learning** — making it
ideal as a college mini-project, internship portfolio piece, or learning exercise.

---

## ✨ Features

- **URL Feature Extraction** — 12 features extracted from URL structure
- **ML Classification** — Logistic Regression vs Random Forest comparison
- **Best Model Selection** — Auto-selects model with highest F1-score
- **Flask Web App** — Simple browser interface to check URLs
- **Confidence Score** — Shows model confidence percentage
- **Clean UI** — Dark cybersecurity-themed HTML/CSS interface
- **JSON API** — `/api/predict` endpoint for programmatic use

---

## 🧰 Technologies Used

| Component       | Technology         |
|-----------------|--------------------|
| Language        | Python 3.8+        |
| Data Handling   | Pandas, NumPy      |
| ML Models       | Scikit-learn       |
| Model Saving    | Joblib             |
| Web Framework   | Flask              |
| Feature Parsing | tldextract, re, urllib |
| Frontend        | HTML5, CSS3        |

---

## 📁 Project Structure

```
phishing-detector/
│
├── dataset/
│   └── urls.csv              # URL dataset (auto-generated or replace with Kaggle data)
│
├── models/
│   └── phishing_model.pkl    # Saved trained model
│
├── static/
│   └── css/
│       └── style.css         # Frontend styles
│
├── templates/
│   └── index.html            # Flask HTML template
│
├── app.py                    # Flask web application
├── train_model.py            # Model training script
├── feature_extraction.py     # URL feature extraction module
├── generate_dataset.py       # Sample dataset generator
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## ⚙️ Features Extracted from URLs

| # | Feature             | Description                              |
|---|---------------------|------------------------------------------|
| 1 | `url_length`        | Total length of the URL                  |
| 2 | `num_dots`          | Number of dots (.)                       |
| 3 | `num_hyphens`       | Number of hyphens (-)                    |
| 4 | `num_slashes`       | Number of forward slashes (/)            |
| 5 | `has_at_symbol`     | Whether URL contains @                   |
| 6 | `has_https`         | Whether URL uses HTTPS                   |
| 7 | `digit_count`       | Number of digits in URL                  |
| 8 | `has_suspicious_words` | login, verify, secure, update, bank   |
| 9 | `has_ip_address`    | Whether URL uses an IP address           |
| 10| `domain_length`     | Length of the domain name                |
| 11| `num_special_chars` | Count of %, =, ?, & characters           |
| 12| `has_subdomain`     | Whether URL has a subdomain              |

---

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Option A: Auto Run (Recommended)
The app will auto-generate the dataset and train the model on first launch:

```bash
python app.py
```

Then open your browser at: **http://127.0.0.1:5000**

---

### Option B: Manual Training First

```bash
# Step 1: Generate dataset (or place your own dataset/urls.csv)
python generate_dataset.py

# Step 2: Train the model
python train_model.py

# Step 3: Start the web app
python app.py
```

---

## 🌐 Using Your Own Dataset

Replace `dataset/urls.csv` with any CSV file that has these columns:

```csv
url,label
https://www.google.com,0
http://phishing-login.tk/verify,1
```

- `label = 0` → Legitimate
- `label = 1` → Phishing

**Recommended Kaggle Datasets:**
- [Phishing Website Dataset](https://www.kaggle.com/datasets/eswarchandt/phishing-website-detector)
- [Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- [Web Page Phishing Detection](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)

---

## 🔌 API Usage

### POST `/api/predict`

```bash
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "http://paypal-secure-login.tk/verify"}'
```

**Response:**
```json
{
  "prediction": 1,
  "label": "Phishing",
  "confidence": 94.5,
  "url": "http://paypal-secure-login.tk/verify"
}
```

---

## 📸 Screenshots

> *(Add screenshots of your running app here)*

| Home Page | Phishing Result | Legitimate Result |
|-----------|----------------|-------------------|
| ![home]() | ![phish]()     | ![legit]()        |

---

## 📈 Model Performance

Both models are trained and compared automatically. Example results:

| Model               | Accuracy | Precision | Recall | F1-Score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression | ~90%     | ~89%      | ~91%   | ~90%     |
| Random Forest       | ~93%     | ~92%      | ~94%   | ~93%     |

*(Results may vary depending on dataset)*

---

## ☁️ Optional Deployment

### Deploy on Render (Free)
1. Push project to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set Build Command: `pip install -r requirements.txt && python train_model.py`
5. Set Start Command: `python app.py`

### Deploy on Replit
1. Go to [replit.com](https://replit.com) → Create Repl → Import from GitHub
2. Open Shell and run: `pip install -r requirements.txt`
3. Run: `python train_model.py` then `python app.py`
4. Use the Replit URL to access your app

---

## 🔮 Future Improvements

- [ ] Add more phishing features (WHOIS lookup, domain age, SSL cert)
- [ ] Use a larger, real-world dataset (50,000+ URLs)
- [ ] Add LSTM/Neural Network model for comparison
- [ ] Real-time URL screenshot analysis
- [ ] Browser extension integration
- [ ] Add user history / URL log
- [ ] Deploy with Gunicorn + Nginx for production
- [ ] Add explainability (SHAP values for feature importance)

---

## 👨‍💻 Author

Built as an educational mini-project demonstrating Machine Learning for Cybersecurity.

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

> **⚠️ Disclaimer:** This project is built purely for educational and demonstration purposes.
> The model is trained on a small sample dataset and should NOT be used as a real security tool.
> Accuracy depends heavily on dataset quality and size.
