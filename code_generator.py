from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("ibm-granite/granite-3.3-2b-instruct")
model = AutoModelForCausalLM.from_pretrained("ibm-granite/granite-3.3-2b-instruct")

def generate_code(prompt, language):
    final_prompt = f"Write {language} code for the following:\n{prompt}"
    inputs = tokenizer(final_prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
