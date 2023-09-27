a = 1
import random
if a == 0:
    scriptur = "And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them."
    words_list = scriptur.split()

    for i in range(len(words_list)):
        words_list[i] =  words_list[i].replace(",","").replace(".","").lower().replace(":","")

    print(words_list)
    secret_word = random.choice(words_list)
    print (secret_word)

secret_word = "moroni"

print("Welcome to the word guessing game!\n")

guess = input("\nWhat is your guess? ".lower())
index = 0

print("Your hint is: ",end="")
for index in range(secret_word):
    if secret_word[index] == guess[index]:
        print (secret_word[index].upper(),end="")
    elif secret_word[index] in guess:
        print (secret_word[index].lower(),end="")
    else:
        print ("_",end="")













print("Your hint is: ",end="")
for letter in secret_word:
    if letter[index] == guess[index]:
        print (letter.upper(),end="")
    elif letter[index] in guess:
        print (letter.lower(),end="")
    else:
        print ("_",end="")
    

    


 