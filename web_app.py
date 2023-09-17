import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

st.markdown("<h1 style='text-align: center;'>Annual Salary Predictor</h1>", unsafe_allow_html=True)

gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ['Director of Marketing', 'Director of Operations', 'Junior Business Analyst', 
            'Junior Business Development Associate', 'Junior Financial Analyst', 
            'Junior Marketing Coordinator', 'Junior Marketing Specialist', 'Junior Operations Analyst', 
            'Junior Project Manager', 'Senior Business Analyst', 'Senior Data Scientist', 
            'Senior Financial Analyst', 'Senior Financial Manager', 'Senior Marketing Analyst', 
            'Senior Marketing Manager', 'Senior Operations Manager', 'Senior Product Designer', 
            'Senior Product Manager', 'Senior Project Coordinator', 'Senior Project Manager', 
            'Senior Software Engineer']

gender = st.radio('Pick your gender', gen_list)
age = st.slider('Pick your age', 21, 55)
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')

if(predict_btn):
    inp1 = int(age)
    inp2 = float(experience)
    inp3 = int(job_list.index(job))
    inp4 = int(edu_list.index(education))
    inp5 = int(gen_list.index(gender))
    X = [inp1, inp2, inp3, inp4, inp5]
    salary = model.predict([X])
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')    
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')


