import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('../saved_model/medical_insurance_model.sav', 'rb'))

# options
Gender = {0: "Female", 1: "Male"}
Smoker = {0: "No", 1: "Yes"}
Region = {0: "Northeast", 1: "Northwest", 2: "Southeast", 3: "Southwest"}

def format_func(dct_name,option):
    return dct_name[option]

def get_medical_insurance_cost(input_data):

    input_data_arr= np.asarray(input_data)
    
    input_data_reshaped = input_data_arr.reshape(1, -1)
    
    cost = model.predict(input_data_reshaped)

    return float(cost)

def main():
    # tite for the app
    st.set_page_config(page_title="Medical Insurance Cost Prediction", page_icon="👨🏻‍⚕️", layout="centered")
    st.title("👨🏻‍⚕️ Medical Insurance Cost Prediction")
    
    # getting input data from user
    form = st.form(key="annotation")

    with form:
        cols = st.columns((1, 1))
        age = cols[0].number_input("Age:", min_value=0,  value=0, step=1)
        sex = cols[1].selectbox("Gender:", Gender.keys(), format_func=lambda x:Gender[ x ])
        bmi = cols[0].number_input("BMI:", min_value=0.0,  value=0.0, step=0.1)
        children = cols[1].number_input("No. of children:", min_value=0,  value=0, step=1)
        smoker = cols[0].selectbox("Smoker:", Smoker.keys(), format_func=lambda x:Smoker[ x ])
        region = cols[1].selectbox("Region:", Region.keys(), format_func=lambda x:Region[ x ])
        submitted = st.form_submit_button(label="Compute Cost")

    # code for prediction
    cost = ""
    
    # create a button
    if submitted:

        status = get_medical_insurance_cost([age, sex, bmi, children, smoker, region])
        st.success(status)

if __name__ == "__main__":
    main()