from transformers import AutoTokenizer, AutoModelForCausalLM
import fitz  # PyMuPDF

tokenizer = AutoTokenizer.from_pretrained("ibm-granite/granite-3.3-2b-instruct")
model = AutoModelForCausalLM.from_pretrained("ibm-granite/granite-3.3-2b-instruct")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def generate_user_stories(pdf_file):
    raw_text = extract_text_from_pdf(pdf_file)
    stories = []
    for line in raw_text.split("\n"):
        if line.strip():
            prompt = f"Convert this into a user story: {line.strip()}"
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=100)
            stories.append(tokenizer.decode(outputs[0], skip_special_tokens=True))
    return "\n".join(stories)
