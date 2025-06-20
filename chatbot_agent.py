import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("ibm-granite/granite-3.3-2b-instruct")
model = AutoModelForCausalLM.from_pretrained("ibm-granite/granite-3.3-2b-instruct")

def run_chatbot():
    user_input = st.text_input("Ask AI:", key="chatbot")
    if user_input:
        inputs = tokenizer(user_input, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=100)
        st.write("🤖 " + tokenizer.decode(outputs[0], skip_special_tokens=True))
