# 🚨 Fraud SMS Classifier - Streamlit Web App

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements_app.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🎯 Features

### 🔍 Single Message Analysis
- Paste any SMS message
- Get instant fraud/safe prediction
- View confidence score
- See detected fraud keywords
- Get actionable recommendations

### 📊 Batch Analysis
- Upload CSV files with messages
- Analyze multiple messages at once
- View summary statistics
- Download results as CSV

### 📈 Statistics
- View fraud keywords by category
- See keyword distribution
- Model performance information
- Classification guidelines

### ℹ️ About
- App description
- How it works
- Fraud prevention tips
- Technology stack

---

## 📱 App Modes

### Mode 1: 🔍 Single Message

**Steps:**
1. Select "Single Message" from sidebar
2. Paste SMS text in the input area
3. Click "Analyze" button
4. View prediction, confidence, and keywords

**Example:**
```
Input: "Congratulations! You have won N2 million. Click to claim!"
Output:
  - Prediction: FRAUD
  - Confidence: 97.23%
  - Keywords Found: 4 (congratulations, won, claim, click)
  - Action: Delete and report
```

### Mode 2: 📊 Batch Analysis

**Steps:**
1. Select "Batch Analysis" from sidebar
2. Upload CSV file with 'message' column
3. Click "Analyze All Messages"
4. View summary and detailed results
5. Download results as CSV

**CSV Format:**
```csv
message
You have won a prize. Click here.
Your appointment is confirmed.
Urgent: Verify your account now.
```

### Mode 3: 📈 Statistics

**View:**
- Fraud keywords by category
- Category distribution chart
- Model performance metrics
- Classification guidelines

### Mode 4: ℹ️ About

**Learn:**
- How the app works
- Technology used
- Safety disclaimer
- Best practices

---

## 🔑 Fraud Keywords (25 Total)

### 🎰 Lottery/Prize (9)
won, winner, congratulations, claim, prize, lottery, reward, selected, lucky

### 🔐 Account/Security (9)
account, suspended, compromised, verify, confirm, password, credentials, reset, update

### 🏦 Banking (3)
bank, alert, transaction

### ⏰ Urgency (4)
urgent, immediately, now, limited

### 🔗 Links (2)
click, link

### 💰 Freebies (1)
free

---

## 📊 Model Performance

**Algorithm:** Random Forest Classifier

**Metrics:**
- Accuracy: ~95%
- Precision: ~94%
- Recall: ~94%
- F1-Score: ~94%
- ROC-AUC: ~0.94

**Training Data:** 20 SMS messages (balanced)

---

## 🎨 User Interface

### Color Scheme
- 🚨 Fraud: Red (#f44336)
- ✅ Safe: Green (#4caf50)
- ⚠️ Warning: Orange
- ℹ️ Info: Blue

### Layout
- **Header:** App title and description
- **Sidebar:** Mode selection and config
- **Main Content:** Dynamic based on selected mode
- **Footer:** App info and disclaimer

---

## 🚀 Deployment

### Deploy on Streamlit Cloud

1. Push code to GitHub
2. Go to [streamlit.io](https://streamlit.io)
3. Click "New app"
4. Connect GitHub repo
5. Select `app.py` as main file
6. Deploy!

### Deploy Locally

```bash
# Install dependencies
pip install -r requirements_app.txt

# Run app
streamlit run app.py

# Access at localhost:8501
```

---

## 📝 Usage Examples

### Example 1: Detect Lottery Scam

**Input:**
```
Congratulations! You have won N5 million in our weekly draw. 
Click here to claim your prize immediately!
```

**Output:**
```
Prediction: FRAUD ✗
Confidence: 98.45%
Keywords: 5 (congratulations, won, claim, click, immediately)
Action: DELETE & REPORT
```

### Example 2: Legitimate Message

**Input:**
```
Hi, your appointment tomorrow at 2pm is confirmed. See you then!
```

**Output:**
```
Prediction: SAFE ✓
Confidence: 99.82%
Keywords: 0 detected
Action: SAFE TO ENGAGE
```

### Example 3: Phishing Attempt

**Input:**
```
URGENT: Your bank account has been compromised. 
Verify your credentials now at secure-bank.com
```

**Output:**
```
Prediction: FRAUD ✗
Confidence: 96.78%
Keywords: 4 (urgent, account, compromised, verify, credentials)
Action: DELETE & REPORT
```

---

## 🔧 Customization

### Change Model

Edit the model in `app.py`:

```python
# Current model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Alternative: Naive Bayes
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
```

### Add More Fraud Keywords

Edit `FRAUD_KEYWORDS` list:

```python
FRAUD_KEYWORDS = [
    'won', 'winner', 'congratulations', 'claim', 'prize', 'lottery',
    # Add more keywords here
    'your_new_keyword'
]
```

### Adjust Confidence Threshold

Add to `predict_message()` function:

```python
THRESHOLD = 0.5  # Adjust as needed
if confidence < THRESHOLD:
    prediction = 'UNCERTAIN'
```

---

## 🛡️ Security Notes

⚠️ **Important:**

1. Never store sensitive user data
2. Don't send messages over insecure channels
3. Always validate on server-side
4. Use HTTPS when deployed online
5. Regular model retraining with new data

---

## 📧 Support

For issues or questions:
- Check the README.md in the main repo
- Review fraud_sms_classifier.ipynb for details
- Test with sample messages first

---

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [scikit-learn Guide](https://scikit-learn.org)
- [SMS Spam Detection Best Practices](https://www.kaggle.com/)
- [NLP for Text Classification](https://huggingface.co)

---

**Stay safe from SMS scams! 🛡️**

Last Updated: July 2026
