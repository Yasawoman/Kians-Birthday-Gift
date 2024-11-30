# Required imports
from textblob import TextBlob
import streamlit as st
from PIL import Image
import random

# Streamlit title and description
st.title("Kian's 26th Birthday Gift")
st.markdown("### Manifesting love for you, in all its shapes & sizes.")

# Function for Magic 8 Ball responses
def magic_8_ball(text):
    # Perform sentiment analysis
    sentiment_score = TextBlob(text).sentiment.polarity

    # Define Magic 8 Ball responses
    positive_responses = [
        "Yes, absolutely! 💖",
        "She loves you! 🌟",
        "You’re her favorite person! 🎉",
    ]
    neutral_responses = [
        "Hmm… it’s complicated. 🤔",
        "Try again later. 🌀",
        "She likes you, but let’s wait and see. 🕰️",
    ]
    negative_responses = [
        "It’s not looking good. 😞",
        "Sorry, but no. 💔",
        "The vibes aren’t great. 🌫️",
    ]

    # Determine response based on sentiment polarity
    if sentiment_score > 0.15:
        response = random.choice(positive_responses)
    elif sentiment_score < -0.15:
        response = random.choice(negative_responses)
    else:
        response = random.choice(neutral_responses)

    # Display the Magic 8 Ball response
    st.markdown(f"🎱 Magic 8 Ball says: **{response}**")

# Streamlit input for user text
st.subheader("🎱 Ask the Magic 8 Ball a question about Yasaman! 🎱 ")
text = st.text_input("Enter your question:", value="Does Yasaman care about me? 🤍🪱")

# Run Magic 8 Ball function if text is provided
if text and text != "Does Yasaman care about me? 🤍🪱":
    magic_8_ball(text)

# Section for uploading and displaying an image
st.subheader("Surprise...she cares a lot 🤍🪱")
uploaded_file = st.file_uploader("Choose an image to upload", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Image successfully uploaded and displayed!")
else:
    st.write("No image uploaded yet. Please upload an image.")