import csv
def read_dictionary(filename):
  """Read the contents of a CSV file into a
  dictionary and return the dictionary.

  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
  
  dictionary = {}

  with open (filename,"rt") as csv_students:
    students = csv.reader(csv_students)
    next(students)
    #{I-Number: Name}

    for student in students:

      dictionary[student[0]] = student[1]

  return dictionary

def main():
  try:
    id_number = input("Enter an I-Number: ")
    print(read_dictionary("students.csv")[id_number])
  except KeyError:
    print("No such student")

if __name__ == "__main__":
  main()