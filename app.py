import streamlit as st
from ai_story_generator import generate_user_stories
from code_generator import generate_code
from test_case_generator import generate_test_cases
from bug_fixer import fix_code
from code_summarizer import summarize_code
from chatbot_agent import run_chatbot

st.set_page_config(page_title="Smart SDLC with AI Enhance", layout="wide")
st.markdown("""
    <style>
        body, .main { background-color: #2e004f !important; color: white !important; }
        .sidebar .sidebar-content { background-color: #1a0033 !important; }
        .chatbot-float {
            position: fixed; bottom: 20px; right: 20px;
            width: 300px; height: 400px;
            background-color: #3a0066;
            border-radius: 10px; padding: 10px;
            box-shadow: 0 0 10px rgba(255,255,255,0.2); z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 💡 Smart SDLC with AI Enhance")
st.markdown("Use AI to accelerate your software development life cycle tasks.")

with st.sidebar:
    st.markdown("### 📚 Library")
    st.info("Upload, manage and access your project files here.")
    st.markdown("### 🕘 History")
    st.success("Track your SDLC activity logs.")

task = st.selectbox("Select a Feature", [
    "AI-Powered Requirement Analysis",
    "Multilingual Code Generation",
    "Test Case Generation",
    "Bug Fixing and Code Correction",
    "Code Summarization and Documentation"
])

if task == "AI-Powered Requirement Analysis":
    uploaded_pdf = st.file_uploader("📄 Upload a Requirement PDF", type=["pdf"])
    if uploaded_pdf:
        with st.spinner("Analyzing Requirements..."):
            user_stories = generate_user_stories(uploaded_pdf)
            st.success("User stories generated!")
            st.code(user_stories)

elif task == "Multilingual Code Generation":
    prompt = st.text_area("📝 Describe the task or user story:")
    language = st.selectbox("🌐 Choose programming language:", ["Python", "JavaScript", "Java"])
    if st.button("Generate Code 💻"):
        code = generate_code(prompt, language)
        st.code(code, language.lower())

elif task == "Test Case Generation":
    code_input = st.text_area("Paste your source code to generate tests")
    if st.button("Generate Test Cases 🧪"):
        test_code = generate_test_cases(code_input)
        st.code(test_code, "python")

elif task == "Bug Fixing and Code Correction":
    buggy_code = st.text_area("Paste buggy code here")
    if st.button("Fix My Code 🛠️"):
        fixed_code = fix_code(buggy_code)
        st.code(fixed_code, "python")

elif task == "Code Summarization and Documentation":
    code = st.text_area("Paste code to generate documentation")
    if st.button("Summarize 📘"):
        summary = summarize_code(code)
        st.success(summary)

st.markdown('<div class="chatbot-float">', unsafe_allow_html=True)
run_chatbot()
st.markdown('</div>', unsafe_allow_html=True)
