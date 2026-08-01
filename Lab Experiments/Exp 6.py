import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt_tab') 
nltk.download('averaged_perceptron_tagger_eng') 

lemmatizer = WordNetLemmatizer()

text = "The boys are running, the girls are writing letters, and the children played games."

words = word_tokenize(text)

pos_tags = nltk.pos_tag(words)

from nltk.corpus import wordnet

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

print("Word\t\tPOS\tLemma")
print("-" * 35)

# Perform Morphological Analysis
for word, tag in pos_tags:
    lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    print(f"{word:12}{tag:8}{lemma}") # Corrected indentation
