import nltk
from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize

nltk.download('punkt')

patterns = [
    (r'.*ing$', 'VBG'),      
    (r'.*ed$', 'VBD'),       
    (r'.*es$', 'VBZ'),      
    (r'.*ould$', 'MD'),      
    (r'.*\'s$', 'NN$'),      
    (r'.*s$', 'NNS'),        
    (r'^[0-9]+$', 'CD'),     
    (r'.*ly$', 'RB'),        
    (r'.*able$', 'JJ'),      
    (r'.*', 'NN')            
]

tagger = RegexpTagger(patterns)

text = "The boys are playing football happily"

tokens = word_tokenize(text)

tagged = tagger.tag(tokens)

print("Rule-Based POS Tagging:\n")

for word, tag in tagged:
    print(f"{word:12} --> {tag}")
