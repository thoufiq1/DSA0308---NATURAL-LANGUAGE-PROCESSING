import sys
sys.path.insert(0, r"C:\p")  # torch is installed here (Windows path-length workaround)

from transformers import MarianMTModel, MarianTokenizer

# Load the English-to-French translation model
model_name = "Helsinki-NLP/opus-mt-en-fr"
print("Loading model (first run downloads it)...")

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# English text
english_text = "Hello, how are you? I am learning NLP."

# Tokenize and translate
inputs = tokenizer(english_text, return_tensors="pt", padding=True)
translated = model.generate(**inputs)

# Decode the result
french_text = tokenizer.decode(translated[0], skip_special_tokens=True)

# Display
print("\nEnglish:", english_text)
print("French: ", french_text)
