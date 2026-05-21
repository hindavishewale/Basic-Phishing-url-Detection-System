# train_model.py
# Trains Logistic Regression and Random Forest models on phishing URL data
# Saves the best model using joblib

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                              recall_score, f1_score, confusion_matrix,
                              classification_report)

from feature_extraction import extract_features, get_feature_names
from generate_dataset import create_sample_dataset


# ─────────────────────────────────────────────
# STEP 1: Load Dataset
# ─────────────────────────────────────────────
def load_dataset(filepath='dataset/malicious_phish.csv'):
    """Load the URL dataset from CSV file."""
    if not os.path.exists(filepath):
        alternative = 'dataset/urls.csv'
        if os.path.exists(alternative):
            print(f"Dataset not found at {filepath}. Using {alternative} instead.")
            filepath = alternative
        else:
            print("Dataset not found. Generating sample dataset...")
            create_sample_dataset()

    df = pd.read_csv(filepath)

    if 'type' in df.columns and 'label' not in df.columns:
        print("Mapping 'type' values to numeric labels...")
        type_map = {
            'phishing': 1,
            'defacement': 1,
            'benign': 0
        }
        df['type'] = df['type'].astype(str).str.lower()
        df['label'] = df['type'].map(type_map)

        unknown_types = df[df['label'].isna()]['type'].unique()
        if len(unknown_types) > 0:
            print(f"Warning: unknown type values found and will be dropped: {unknown_types}")
            df = df[df['label'].notna()].copy()
            df['label'] = df['label'].astype(int)

    if 'label' not in df.columns:
        raise ValueError(
            f"Dataset must contain a 'label' column or a 'type' column that can be mapped." \
            f" Found columns: {list(df.columns)}"
        )

    print(f"✅ Dataset loaded: {len(df)} rows")
    print(f"   Phishing URLs : {df[df['label'] == 1].shape[0]}")
    print(f"   Legitimate URLs: {df[df['label'] == 0].shape[0]}")
    return df


# ─────────────────────────────────────────────
# STEP 2: Extract Features
# ─────────────────────────────────────────────
def build_feature_matrix(df):
    """Extract features from each URL and build a DataFrame."""
    print("\n⚙️  Extracting features from URLs...")
    feature_list = []

    for url in df['url']:
        features = extract_features(str(url))
        feature_list.append(features)

    feature_df = pd.DataFrame(feature_list, columns=get_feature_names())

    # Drop rows with missing values (if any)
    feature_df = feature_df.fillna(0)

    print(f"✅ Features extracted: {feature_df.shape[1]} features per URL")
    return feature_df


# ─────────────────────────────────────────────
# STEP 3: Train Models
# ─────────────────────────────────────────────
def evaluate_model(name, model, X_test, y_test):
    """Print evaluation metrics for a trained model."""
    y_pred = model.predict(X_test)

    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec  = recall_score(y_test, y_pred, zero_division=0)
    f1   = f1_score(y_test, y_pred, zero_division=0)
    cm   = confusion_matrix(y_test, y_pred)

    print(f"\n{'='*45}")
    print(f"  Model: {name}")
    print(f"{'='*45}")
    print(f"  Accuracy  : {acc:.4f}")
    print(f"  Precision : {prec:.4f}")
    print(f"  Recall    : {rec:.4f}")
    print(f"  F1-Score  : {f1:.4f}")
    print(f"\n  Confusion Matrix:")
    print(f"  {cm}")
    print(f"\n  Classification Report:")
    print(classification_report(y_test, y_pred,
                                 target_names=['Legitimate', 'Phishing']))

    return f1  # Return F1 for model comparison


def train_and_save():
    """Full training pipeline: load → features → train → evaluate → save."""

    # Load data
    df = load_dataset()

    # Build features
    X = build_feature_matrix(df)
    y = df['label'].values

    # Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\n📊 Train size: {len(X_train)} | Test size: {len(X_test)}")

    # ── Model 1: Logistic Regression ──
    print("\n🔄 Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    lr_f1 = evaluate_model("Logistic Regression", lr_model, X_test, y_test)

    # ── Model 2: Random Forest ──
    print("\n🔄 Training Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_f1 = evaluate_model("Random Forest", rf_model, X_test, y_test)

    # ── Select Best Model ──
    print("\n" + "="*45)
    if rf_f1 >= lr_f1:
        best_model = rf_model
        best_name  = "Random Forest"
    else:
        best_model = lr_model
        best_name  = "Logistic Regression"

    print(f"🏆 Best Model: {best_name} (F1 = {max(rf_f1, lr_f1):.4f})")

    # ── Save Best Model ──
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_model, 'models/phishing_model.pkl')
    print(f"\n💾 Model saved to: models/phishing_model.pkl")
    print("\n✅ Training complete! Run app.py to start the web app.\n")


if __name__ == "__main__":
    train_and_save()
