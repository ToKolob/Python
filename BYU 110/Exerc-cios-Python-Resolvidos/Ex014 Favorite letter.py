letter_favorite = str(input("What is your favorite letter?"))
len_letter = len(letter_favorite)
while len_letter != 1:
    letter_favorite = input("Sorry, What is your favorite letter?")
    len_letter = len(letter_favorite)

word = "pneumonoultramicroscopicsilicovolcanoconiosis"
for letter in word:
    if letter == letter_favorite.lower():
        print("_",end="")
    else:
        print(letter.lower(),end="")

