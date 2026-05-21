# app.py
# Flask web application for Phishing URL Detection
# Run this file to start the web server: python app.py

import os
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify
from feature_extraction import extract_features, get_feature_names

# ── Initialize Flask App ──
app = Flask(__name__)

# ── Load the trained model ──
MODEL_PATH = 'models/phishing_model.pkl'

def load_model():
    """Load the saved ML model. Trains it if not found."""
    if not os.path.exists(MODEL_PATH):
        print("⚠️  Model not found. Training model first...")
        from train_model import train_and_save
        train_and_save()
    return joblib.load(MODEL_PATH)

model = load_model()
print("✅ Model loaded successfully!")


# ── Helper: Predict a single URL ──
def predict_url(url):
    """Extract features from URL and return prediction."""
    features = extract_features(url)
    feature_df = pd.DataFrame([features], columns=get_feature_names())
    prediction = model.predict(feature_df)[0]
    probability = model.predict_proba(feature_df)[0]

    return {
        'prediction': int(prediction),
        'label': 'Phishing' if prediction == 1 else 'Legitimate',
        'confidence': round(float(max(probability)) * 100, 2)
    }


# ── Routes ──

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle URL prediction request from the form."""
    url = request.form.get('url', '').strip()

    if not url:
        return render_template('index.html',
                               error="Please enter a URL to check.")

    # Add http:// prefix if missing (for feature extraction)
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        result = predict_url(url)
        return render_template('index.html',
                               url=url,
                               result=result)
    except Exception as e:
        return render_template('index.html',
                               error=f"Error processing URL: {str(e)}")


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """JSON API endpoint for URL prediction."""
    data = request.get_json()
    url = data.get('url', '').strip()

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        result = predict_url(url)
        result['url'] = url
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ── Run the App ──
if __name__ == '__main__':
    print("\n" + "="*50)
    print("  🔐 Phishing URL Detection System")
    print("  Running at: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(debug=True, host='127.0.0.1', port=5000)
