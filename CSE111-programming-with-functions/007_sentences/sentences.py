from random import choice
# As exceeding the Requirements I added a second prepositional phrase to the make_sentence function and a loop in the main function

run_again = "y"

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

# Function to get a preposition randomly
def get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"
    ]
    return choice(prepositions)

# Function to get a prepositional phrase
def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    noun = get_noun(quantity)
    determiner = get_determiner(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

# Function to make a sentence based on the quantity and tense
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)    
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner} {noun} {prepositional_phrase} {verb} {prepositional_phrase2}."
    return sentence.capitalize()

# The main function do not need explanations, ;) 
def main():
    quantity = [1,2]
    verb_tenses = ["past", "present", "future"]
    for quantity in quantity:
        for tense in verb_tenses:
            print(make_sentence(quantity, tense))

while run_again == "y":
    main()
    run_again = input("Do you want to run the program again? (y/n)") or "y"