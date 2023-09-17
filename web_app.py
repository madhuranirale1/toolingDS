import pickle
import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('salaryData.csv')
#filter only relevant data
data = data.groupby('Job Title').filter(lambda x : len(x)>4)

color_styles = [
    ('red', 'color: red; font-size: 48px;'),
    ('orange', 'color: orange; font-size: 48px;'),
    ('blue', 'color: blue; font-size: 48px;')
]

# Create the centered heading with colored text and font size
st.markdown(
    """
    <div style="text-align: center;">
        <span style="{}">Annual</span>
        <span style="{}">Salary</span>
        <span style="{}">Predictor</span>
        <span style="font-size: 48px;">&#x1F4B0;</span> <!-- Money Emoji -->
    </div>
    """.format(*[style for _, style in color_styles]),
    unsafe_allow_html=True
)

st.write("## What does our data look like?")

# Display the first few rows of the dataset
st.write("### Take a peek")
st.write(data.head())

# Display summary statistics
st.write("### Summary Statistics")
st.write(data.describe())

# Display a heatmap to visualize correlations
st.write("### Correlation Heatmap")
corr_matrix = data.corr()
plt.figure(figsize=(2, 2))
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Create interactive scatter plots using Plotly Express
st.write("### Interactive Scatter Plot")
x_axis = st.selectbox("Select X-axis", data.columns)
y_axis = st.selectbox("Select Y-axis", data.columns)
fig = px.scatter(data, x=x_axis, y=y_axis, title=f"{x_axis} vs. {y_axis}")
st.plotly_chart(fig)

# Create a histogram
st.write("### Histogram")
feature = st.selectbox("Select a feature", data.columns)
fig, ax = plt.subplots()
sns.histplot(data[feature], kde=True, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

st.write("## Let's predict now!")

#unpickle our model dumped in the modeling file
model = pickle.load(open('model.pkl', 'rb'))

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

#create input widgets
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


