import streamlit as st
from utils.inference import predict_new
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, forest_model
from utils.CustomerData import CustomerData

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title=APP_NAME, layout="centered")
st.title(f"{APP_NAME} v{VERSION}")
st.write("Churn Prediction using Random Forest Model")
st.divider()

# -------------------------
# API Key Authentication
# -------------------------
st.subheader("🔐 Authentication")
api_key = st.text_input("Enter API Key", type="password", placeholder="X-API-Key")

st.divider()

# -------------------------
# User Inputs
# -------------------------
st.subheader("📋 Customer Information")

col1, col2 = st.columns(2)

with col1:
    creditscore = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure (Years)", min_value=0, max_value=20, value=5)

with col2:
    balance = st.number_input("Balance", min_value=0.0, value=0.0)
    numofproducts = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
    hascrcard = st.selectbox("Has Credit Card", [0, 1])
    isactivemember = st.selectbox("Is Active Member", [0, 1])
    estimatedsalary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

st.divider()

# -------------------------
# Prediction Button
# -------------------------
if st.button("🔍 Predict Churn", use_container_width=True):

    # Auth check (mirrors FastAPI's verify_api_key dependency)
    if not api_key:
        st.error("❌ Please enter an API key.")
    elif api_key != SECRET_KEY_TOKEN:
        st.error("🚫 You are not authorized to use this app. Invalid API key.")
    else:
        data = CustomerData(
            creditscore=creditscore,
            geography=geography,
            gender=gender,
            age=age,
            tenure=tenure,
            balance=balance,
            numofproducts=numofproducts,
            hascrcard=hascrcard,
            isactivemember=isactivemember,
            estimatedsalary=estimatedsalary,
        )

        try:
            result = predict_new(
                data=data,
                preprocessor=preprocessor,
                model=forest_model,
            )
            st.success("Prediction Completed ✅")
            st.json(result)

        except Exception as e:
            st.error(f"⚠️ Prediction Error: {e}")
