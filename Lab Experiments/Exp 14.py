grammar = {
    "S": ["NP VP"],
    "NP": ["Det N"],
    "VP": ["V"],
    "Det": ["the"],
    "N_singular": ["cat", "dog"],
    "N_plural": ["cats", "dogs"],
    "V_singular": ["eats", "runs"],
    "V_plural": ["eat", "run"]
}

def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) != 3:
        return False

    determiner, noun, verb = words

    if noun in grammar["N_singular"] and verb in grammar["V_singular"]:
        return True

    if noun in grammar["N_plural"] and verb in grammar["V_plural"]:
        return True

    return False


sentences = ["the cat eats", "the cats eat",
             "the cat eat", "the cats eats"]

for s in sentences:
    print(check_agreement(s))
