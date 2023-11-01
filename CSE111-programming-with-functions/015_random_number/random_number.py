from random import uniform
def main():
  numbers = [16.2, 75.1, 52.3]
  print(numbers)

  append_random_numbers(numbers)

  print(numbers)

  append_random_numbers(numbers, 3)

  print(numbers)


#incremet a randomic number from 0 to 100 with a step of 0.1
def append_random_numbers(numbers_list, quantity = 1):
  for _ in range(quantity):
    numbers_list.append( round(uniform(0, 100),1))

if __name__ == "__main__":
  main()
