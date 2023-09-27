#to input a secret word I choose to insert an escripture that get a random word

secret_word = "moroni"
index = 0
guess = ""
guess_count = 0
import random

scriptur = "And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them."
words_list = scriptur.split()

for i in range(len(words_list)):
        words_list[i] =  words_list[i].replace(",","").replace(".","").lower().replace(":","")
secret_word = random.choice(words_list)


print("Welcome to the word guessing game!\n")

print("Your hint is: ",end="")
for i in secret_word:
    print("_ ",end="")


while guess != secret_word:
    guess = input("\nWhat is your guess? ".lower())

    if len(guess) == len(secret_word):
        print("Your hint is: ",end="")
        for letter in guess:

            if letter == secret_word[index]:
                print(letter.upper(),end=" ")

            elif letter in secret_word:
                print(letter.lower(),end=" ")

            else:
                print("_",end=" ")
            index = index + 1

    else:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    guess_count = guess_count + 1
    index = 0

print ("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")