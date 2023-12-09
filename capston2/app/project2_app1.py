import streamlit as st
from streamlit_lottie import st_lottie 
import json

# Set overall page style
st.set_page_config(
    page_title="Employee Churn Prediction",
    layout="wide",
    initial_sidebar_state="auto"
)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("Animation.json")

# Apply custom CSS styles
st.markdown(
    """
    <style>
        body {
            margin: 50px;
            background-image: url("12.jpg");
            background-repeat: no-repeat;
            background-size: cover;
            padding: 20px;
        }
        .main-container {
            display: flex;
            flex-direction: row;
        }
        .animation-container {
            display: flex;
            justify-content: flex-end;
            align-items: flex-start;
            width: 400px;
            height: 400px;
        }
        .content-container {
            flex: 1;
            padding: 20px;
        }
        .button-container {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        @keyframes fade-in {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        .welcome {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: cursive;
        }
        .objective {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: cursive;
            white-space: pre-line;
        }
        .inner-header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            font-family: cursive;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("Welcome to Our Prediction System")
# Inner header about employee churn
st.markdown('<h2 class="inner-header">Employee Churn</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="objective">The objective of this project is to\npredict whether an employee will leave the company or not.\nBy analyzing various factors and using machine learning algorithms,\nwe aim to provide insights into employee churn and help organizations\nmake data-driven decisions.</p>',
    unsafe_allow_html=True
)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Content container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Group members section
st.header("Group Members")
members = ["Afnan", "Hussan", "Marwah", "Rahaf", "Salma", "Waad", "Aeshah", "Atheer", "Sarah"]
for i in range(0, len(members), 2):
    if i + 1 < len(members):
        st.markdown(f'<p class="welcome">{members[i]}, {members[i+1]}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="welcome">{members[i]}</p>', unsafe_allow_html=True)

# Button to go to the prediction page
st.markdown('<div class="button-container"><a href="http://localhost:8502/" class="button">Let\'s Predict</a></div>', unsafe_allow_html=True)

# Close content container
st.markdown('</div>', unsafe_allow_html=True)

# Close main container
st.markdown('</div>', unsafe_allow_html=True)

# Lottie animation container
st.markdown('<div class="animation-container">', unsafe_allow_html=True)
st_lottie(lottie_coding, width=400, height=400, speed=1, reverse=False, loop=True)
st.markdown('</div>', unsafe_allow_html=True)