import streamlit as st
from prediction_helper import predict
from PIL import Image

# Set up session state to hold user inputs and navigation
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Page 1: Demographic Information
if st.session_state.page == 1:
    st.set_page_config(page_title="🎉 Health Insurance Predictor - Page 1", layout="wide")
    st.markdown("""
        <style>
            .stApp {
                background-color: #FBE9E7;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center; color:#B71C1C;">Demographic Information</h1>', unsafe_allow_html=True)

    with st.form("demo_form"):
        age = st.slider('🎂 Age', min_value=18, max_value=100, value=25)
        income = st.slider('💰 Income in Lakhs', min_value=0, max_value=200, value=10)
        gender = st.selectbox('⚧️ Gender', ['Male', 'Female'])
        marital_status = st.selectbox('💍 Marital Status', ['Married', 'Unmarried'])
        employment_status = st.selectbox('💼 Employment Status', ['Salaried', 'Self-Employed', 'Freelancer'])
        dependants = st.number_input('👨‍👩‍👦 Number of Dependants', min_value=0, step=1, max_value=20)

        submitted = st.form_submit_button("Next ➡️")
        if submitted:
            st.session_state.form_data.update({
                'Age': age,
                'Income in Lakhs': income,
                'Gender': gender,
                'Marital Status': marital_status,
                'Employment Status': employment_status,
                'Number of Dependants': dependants
            })
            st.session_state.page = 2
            st.rerun()

# Page 2: Disease and General Info
elif st.session_state.page == 2:
    st.markdown("""
        <style>
            .stApp {
                background-color: #FFF3E0;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center; color:#E65100;">Disease and General Information</h1>', unsafe_allow_html=True)

    with st.form("disease_form"):
        smoking = st.selectbox('🚬 Smoking Status', ['No Smoking', 'Regular', 'Occasional'])
        medical = st.selectbox('🏥 Medical History', [
            'No Disease', 'Diabetes', 'High Blood Pressure', 'Diabetes & High BP',
            'Thyroid', 'Heart Disease', 'BP & Heart Disease', 'Diabetes & Thyroid',
            'Diabetes & Heart Disease'])
        bmi = st.selectbox('⚖️ BMI Category', ['Normal', 'Obesity', 'Overweight', 'Underweight'])
        genetical_risk = st.slider('🧬 Genetical Risk (0-5)', 0, 5, 2)

        submitted = st.form_submit_button("Next ➡️")
        if submitted:
            st.session_state.form_data.update({
                'Smoking Status': smoking,
                'Medical History': medical,
                'BMI Category': bmi,
                'Genetical Risk': genetical_risk
            })
            st.session_state.page = 3
            st.rerun()

# Page 3: Region and Insurance Plan
elif st.session_state.page == 3:
    st.markdown("""
        <style>
            .stApp {
                background-color: #E8F5E9;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center; color:#2E7D32;">Region & Plan Information</h1>', unsafe_allow_html=True)

    region = st.selectbox('🌎 Region', ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
    plan = st.selectbox('📜 Insurance Plan', ['Bronze', 'Silver', 'Gold'])

    if st.button("🎯 Predict Insurance Cost"):
        st.session_state.form_data.update({
            'Region': region,
            'Insurance Plan': plan
        })
        st.session_state.page = 4
        st.rerun()

# Page 4: Prediction Display
elif st.session_state.page == 4:
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(to right, #E3F2FD, #E1BEE7);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center; color:#4A148C;">🎉 Prediction Result</h1>', unsafe_allow_html=True)

    st.markdown("#### ✍️ Entered Information:")
    for key, val in st.session_state.form_data.items():
        st.write(f"**{key}:** {val}")

    try:
        prediction = predict(st.session_state.form_data)
        prediction_text = f"💰 Predicted Health Insurance Cost: {float(prediction):,.2f} $"
    except Exception as e:
        prediction_text = f"Prediction Error: {str(e)}"

    st.success(prediction_text)

    if st.button("✏️ Edit Information"):
        st.session_state.page = 1
        st.rerun()