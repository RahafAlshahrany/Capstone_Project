import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

# Load the model
filename = "rf_model.pkl"
model=pickle.load(open(filename, "rb"))

# Function to load the CSV file
def load_data(file):
    df = pd.read_csv(file)
    return df

# Function to perform fraud detection prediction
def predict_fraud(data, entry=None):
    if 'Class' in data.columns:
        X = data.drop('Class', axis=1)
    else:
        X = data

    if entry:
        # Convert entry dictionary to numeric array-like format
        entry_array = np.array(list(entry.values())).reshape(1, -1)

        # Predict for a specific entry
        prediction = model.predict(entry_array)
        return prediction
    else:
        # Predict for all entries
        predictions = model.predict(X)
        return predictions

# Main function
def main():
    st.title("Fraud Credit Card Detection")

    # Sidebar options
    st.sidebar.title("Options")
    option = st.sidebar.radio("Select an option", ("Upload CSV", "Enter Values"))

    if option == "Upload CSV":
        file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
        if file is not None:
            data = load_data(file)

            st.subheader("CSV File")
            st.write(data)

            predictions = predict_fraud(data)
            st.subheader("Predictions")
            st.write(predictions)

    elif option == "Enter Values":
        st.sidebar.subheader("Enter Credit Card Details")

        # Collect credit card details from the user
        # Adjust the input fields based on your dataset's columns
        entry = {}

        for column in ['V12', 'V17', 'V14', 'V16', 'V10', 'V11', 'V18', 'V9', 'V4', 'V7']:
            entry[column] = st.sidebar.text_input(column)

        if st.sidebar.button("Predict"):
            data = pd.DataFrame([entry])
            predictions = predict_fraud(data, entry)
            st.subheader("Prediction")
            st.write(predictions[0])

# Run the app
if __name__ == '__main__':
    main()