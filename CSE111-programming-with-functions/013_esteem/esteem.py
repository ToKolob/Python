def question(positive=True):
  # Return 1, 2, 3, or 4 based on user input
  # If positive is True, return 1, 2, 3, or 4
  # If positive is False, return 4, 3, 2, or 1


  answer = 0
  while answer != "D" and answer != "d" and answer != "a" and answer != "A":
    answer = input("Enter D, d, a, or A:")

    if answer == "A":
      points = 3
    elif answer == "a":
      points = 2
    elif answer == "d":
      points = 1
    else:
      points = 0

  if positive:
    
    return points
  else:
    return 3 - points

def main():
  # The Rosenberg Self-Esteem Scale

  print ("""This program is an implementation of the Rosenberg
  Self-Esteem Scale. This program will show you ten
  statements that you could possibly apply to yourself.
  Please rate how much you agree with each of the
  statements by responding with one of these four letters:
        
  D means you strongly disagree with the statement.
  d means you disagree with the statement.
  a means you agree with the statement.
  A means you strongly agree with the statement.         
         """)

  sum = 0

  print("1. I feel that I am a person of worth, at least on an equal plane with others.")
  sum += question()

  print("2. I feel that I have a number of good qualities.")
  sum += question()

  print("3. All in all, I am inclined to feel that I am a failure.")
  sum += question(False)

  print("4. I am able to do things as well as most other people.")
  sum += question()

  print("5. I feel I do not have much to be proud of.")
  sum += question(False)

  print("6. I take a positive attitude toward myself.")
  sum += question()

  print("7. On the whole, I am satisfied with myself.")
  sum += question()

  print("8. I wish I could have more respect for myself.")
  sum += question(False)

  print("9. I certainly feel useless at times.")
  sum += question(False)

  print("10. At times I think I am no good at all.")
  sum += question(False)

  print("")
  print("Your total score is ", sum)
  print("A score below 15 may indicate problematic low self-esteem.")


if __name__ == "__main__":
  
  main()



