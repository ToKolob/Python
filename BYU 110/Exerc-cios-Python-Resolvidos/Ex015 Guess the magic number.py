play_again = "yes"
while play_again == "yes":
    import random
    magic_number = random.randint(1,10)
    print(magic_number)
    guess_number = int(input("What is the magic number? "))
    tries = 1
    while guess_number != magic_number:
        if guess_number > magic_number:
            print("Lower!")
        else:
            print("Higher!")
        guess_number = int(input("What is the magic number? "))
        tries = tries + 1
    print("You guessed it!")
    print(f"and you just needed {tries} attempts!!")

    valid_options = "yes", "no"
    play_again = ""
    while play_again not in valid_options:
        play_again = input("Do you wanna play again? ").lower()
        
print("Thank you for playing. Goodbye.")







