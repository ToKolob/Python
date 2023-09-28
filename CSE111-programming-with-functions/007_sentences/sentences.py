from random import choice

# Function to get a determiner based on the quantity
def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = choice(determiners)
    return determiner

# Function to get a noun based on the quantity
def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return choice(words)

# Function to get a verb based on the quantity and tense
def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return choice(verbs)

# Function to make a sentence based on the quantity and tense
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner} {noun} {verb}."
    return sentence.capitalize()

def main():
    quantity = [1,2]
    verb_tenses = ["past", "present", "future"]
    for quantity in quantity:
        for tense in verb_tenses:
            print(make_sentence(quantity, tense))

main()