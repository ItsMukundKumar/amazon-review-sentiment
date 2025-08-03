<h1>🛍️ Amazon Review Sentiment Analysis</h1>
<spam>This is a simple machine learning project that predicts the **sentiment** of Amazon product reviews (Good or Bad) using a trained model and a text vectorizer.
</spam>

<h3>🔍 Features</h3>
<spam>
- Input a product review text
- Pre-trained ML model using Scikit-learn
- CountVectorizer for text transformation
- Streamlit web app for interactive UI
- Returns prediction: Good or Bad
</spam>
<h3>🗂️ Project Structure</h3>

<spam>
amazon-review-sentiment/
├── app.py                  # Main Streamlit application
├── amazon_review_model.pkl # Trained sentiment model
├── vectorizer.pkl          # Fitted CountVectorizer
├── requirements.txt        # Python dependencies
└── README.md               # Project description
</spam>

<h4>🚀 How to Run This Project</h4>

<h5>1. Clone the repository</h5>

<spam>
git clone https://github.com/YourUsername/amazon-review-sentiment.git
cd amazon-review-sentiment
</spam>

<h5>2. Install the dependencies</h5>

<spam>
pip install -r requirements.txt
</spam>

<h5>
3. Run the Streamlit app
</h5>

<spam>
streamlit run app.py
</spam>

<h3>Sample Reviews</h3>
<spam>
Review: "I love this product! Works exactly as expected."  
Prediction: Good

Review: "Terrible experience. It broke after one use."  
Prediction: Bad
</spam>

<h3>📦 Requirements</h3>

<spam>
- Python 3.9+
- streamlit
- scikit-learn
- joblib
</spam>
