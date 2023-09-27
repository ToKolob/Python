secret_word = "moroni"
guesses_count = 0
print("Welcome to the word guessing game!\n")

guess = input("\nWhat is your guess? ")
while guess.lower() != secret_word:
    print("Your guess was not correct.")
    guess = input("\nWhat is your guess? ")
    guesses_count = guesses_count + 1

print("Congratulations! You guessed it!")
print(f"It took you {guesses_count} guesses.")




