import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, DefaultTagger

nltk.download('treebank')

train_data = treebank.tagged_sents()

default_tagger = DefaultTagger('NN')

tagger = UnigramTagger(train_data, backoff=default_tagger)

sentence = "The quick brown fox jumps over the lazy dog".split()

tagged = tagger.tag(sentence)

print("Stochastic POS Tagging\n")
for word, tag in tagged:
    print(f"{word:10} --> {tag}")
