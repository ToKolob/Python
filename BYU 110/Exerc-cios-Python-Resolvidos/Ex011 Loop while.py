

valid_options = ["yes", "no"]
answer = str(input("May I have a piece od candy? ").lower())
while answer not in valid_options or answer == "no":
    answer = str(input("May I have a piece od candy? ").lower())
print("Thank You.")



num = int(input("Please type a positive number: "))
while num < 0:
    print ("Sorry, that is a negative number. Please try again.")
    num = int(input("Please type a positive number: "))
print(f"The number is: {num}.")