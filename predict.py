"""
Fraud SMS Classifier - Prediction Script
Standalone script for making predictions on new SMS messages
"""

import re
import joblib
import pickle
from pathlib import Path

# Fraud keywords for insight
FRAUD_KEYWORDS = [
    'won', 'winner', 'congratulations', 'claim', 'prize', 'lottery',
    'urgent', 'verify', 'confirm', 'account', 'suspended', 'compromised',
    'click', 'link', 'update', 'reset', 'password', 'credentials',
    'bank', 'alert', 'transaction', 'reward', 'selected', 'lucky',
    'immediately', 'now', 'limited', 'free'
]


def preprocess_text(text):
    """
    Preprocess SMS text for classification
    """
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def count_fraud_keywords(text):
    """Count fraud keywords in message"""
    text_lower = text.lower()
    return sum(1 for keyword in FRAUD_KEYWORDS if keyword in text_lower)


def extract_fraud_keywords(text):
    """Extract which fraud keywords are present"""
    text_lower = text.lower()
    found_keywords = [kw for kw in FRAUD_KEYWORDS if kw in text_lower]
    return found_keywords


def predict_fraud(message, model_path='models/random_forest_model.joblib', 
                  vectorizer_path='models/tfidf_vectorizer.joblib'):
    """
    Predict if an SMS is fraudulent
    
    Args:
        message: SMS text to classify
        model_path: Path to trained model
        vectorizer_path: Path to TF-IDF vectorizer
    
    Returns:
        Dictionary with prediction details
    """
    try:
        # Load model and vectorizer
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        
        # Preprocess message
        cleaned = preprocess_text(message)
        
        # Vectorize
        X = vectorizer.transform([cleaned])
        
        # Predict
        prediction = model.predict(X)[0]
        confidence = model.predict_proba(X)[0][int(prediction)]
        
        # Get fraud keywords
        fraud_kw_count = count_fraud_keywords(message)
        found_keywords = extract_fraud_keywords(message)
        
        return {
            'message': message[:100] + '...' if len(message) > 100 else message,
            'prediction': 'FRAUD' if prediction == 1 else 'SAFE',
            'confidence': f"{confidence*100:.2f}%",
            'fraud_keywords_detected': fraud_kw_count,
            'keywords_found': found_keywords if found_keywords else 'None',
            'recommendation': 'Delete and report' if prediction == 1 else 'Safe to engage'
        }
    
    except FileNotFoundError:
        return {
            'error': 'Model files not found. Please run the notebook first to train the model.',
            'required_files': [model_path, vectorizer_path]
        }


def interactive_demo():
    """Interactive demo for testing messages"""
    print("\n" + "="*70)
    print("FRAUD SMS CLASSIFIER - INTERACTIVE DEMO")
    print("="*70)
    print("\nEnter SMS messages to classify (type 'quit' to exit):\n")
    
    while True:
        message = input("📱 Enter SMS message: ").strip()
        
        if message.lower() == 'quit':
            print("\n✓ Exiting classifier. Stay safe from scams!")
            break
        
        if not message:
            print("⚠️  Please enter a valid message.\n")
            continue
        
        result = predict_fraud(message)
        
        if 'error' in result:
            print(f"❌ {result['error']}\n")
        else:
            print(f"\n{'─'*70}")
            print(f"Prediction: {result['prediction']}")
            print(f"Confidence: {result['confidence']}")
            print(f"Fraud Keywords: {result['fraud_keywords_detected']}")
            if result['keywords_found'] != 'None':
                print(f"Keywords Found: {', '.join(result['keywords_found'])}")
            print(f"Recommendation: {result['recommendation']}")
            print(f"{'─'*70}\n")


if __name__ == "__main__":
    interactive_demo()
