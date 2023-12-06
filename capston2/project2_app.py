import streamlit as st
import pickle
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

st.sidebar.title('Leaving The Company Prediction')
html_temp = """
<div style="background-color:blue;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

avg_monthly_hours=st.sidebar.slider("What is your average monthly hours", 40, 400, step=1)
satisfaction_level=st.sidebar.slider('How much is your satisfaction level?',0, 100, step=1)
last_evaluation=st.sidebar.slider("What was your last evaluation?", 0, 100, step=1)
num_project=st.sidebar.slider("Select the number of projects", 1,10, step=1)
time_in_company=st.sidebar.slider("How many years did you spend in the company?",1,20, step=1)
salary=st.sidebar.selectbox("Which category describes you salary?", ('Low', 'Medium', 'High'))
department=st.sidebar.selectbox("Which department do you work in?", ('Sales', 'Technical', 'Support','IT', 'RandD', 'Product manager','Marketing', 'Accounting', 'HR', 'Management'))

rf_model=pickle.load(open("model.pkl","rb"))
transformer = pickle.load(open('transformer.pkl', 'rb'))


my_dict = {
    "average_montly_hours": avg_monthly_hours,
    "satisfaction_level":satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": num_project, 
    "time_spend_company": time_in_company,
    "salary": salary, 
    "Departments": department
}

df = pd.DataFrame.from_dict([my_dict])


st.header("Your information as you selected is below")
st.table(df)

df2 = transformer.transform(df)


st.subheader("Press predict when you're ready")

if st.button("Predict"):
    prediction = rf_model.predict(df2)
    st.success("The likelyhood of you leaving the company is: {}. ".format(int(prediction[0])))
