import streamlit as st
from prompt_template import build_prompt
import google.generativeai as genai
import os

# Set API Key from secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def generate_response(prompt, model="gemini-1.5-pro"):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Scholarship Eligibility Analyzer", layout="centered")

st.title("🎓 Scholarship Eligibility Analyzer")

with st.form("eligibility_form"):
    name = st.text_input("Full Name")
    age = st.text_input("Age")
    qualifications = st.text_area("Academic Qualifications")
    gpa = st.text_input("GPA")
    income = st.text_input("Family Income")
    activities = st.text_area("Extracurricular Activities")
    other_info = st.text_area("Other Info")

    submitted = st.form_submit_button("Analyze")

if submitted:
    prompt = build_prompt(name, age, qualifications, gpa, income, activities, other_info)
    with st.spinner("Analyzing eligibility..."):
        try:
            result = generate_response(prompt)
            st.success("✅ Analysis Complete!")
            st.markdown(result)
        except Exception as e:
            st.error(f"❌ Error: {e}")
