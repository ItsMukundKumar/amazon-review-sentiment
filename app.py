import streamlit as st
import joblib

# Load vectorizer and model
vectorizer = joblib.load('vectorizer.pkl')
model = joblib.load('amazon_review_model.pkl')

# Mapping
label_map = {
    1: 'Good',
    0: 'Bad'
}

# Streamlit UI
st.set_page_config(page_title="Amazon Review Sentiment", layout="centered")
st.title("🛍️ Amazon Review Sentiment Classifier")
st.markdown("### Enter your review below 👇")

# Input
review = st.text_area("✏️ Your Review:", placeholder="Type your product review here...")

# Predict Button
if st.button("🔍 Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review to analyze.")
    else:
        # Transform and predict
        X_new = vectorizer.transform([review])
        prediction = model.predict(X_new)
        sentiment = label_map[prediction[0]]

        # Show Result
        if sentiment == 'Good':
            st.success("✅ Predicted Sentiment: **Good**")
        else:
            st.error("❌ Predicted Sentiment: **Bad**")
