import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.

  Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
      to use as the keys in the dictionary.
  Return: a compound dictionary that contains
    the contents of the CSV file.
  """
  dictionary = {}
  with open (filename, 'rt') as csv_file:
    dict_reader = csv.reader(csv_file)
    next(dict_reader)
    for line in dict_reader:
      key = line[key_column_index]
      dictionary[key] = line
            


  return dictionary
  
def main():
  try:
    products_dict = read_dictionary('products.csv', 0)
    number_of_items = 0
    subtotal = 0  

    with open ('request.csv', 'rt') as request_file:
      request_reader = csv.reader(request_file)
      next(request_reader)
      print("Inkom Emporium \n")
      for line in request_reader:
        product_name = products_dict[line[0]][1]
        requested_quantity = line[1]
        number_of_items += int(requested_quantity)
        product_price = products_dict[line[0]][2]
        subtotal += int(requested_quantity) * float(product_price)
        print(f"{product_name}: {requested_quantity} @ {product_price}")
    
    print("\n")
    print(f"Number of Items: {number_of_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {subtotal * 0.06:.2f}")
    print(f"Total: {subtotal * 1.06:.2f}")
    print()
    print("Thanks for shopping at the Inkom Emporium!")
      
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%a %b   %d %I:%M:%S %Y}")

  except KeyError as e:
    print(f"Error: unknown product ID in request.csv file, {e}")

  except FileNotFoundError as e:
    print(f"Error: missing file \n[Errno 2] No such file or directory: '{e.filename}'")

                                             


if __name__ == "__main__":
  main()