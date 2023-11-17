import csv
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
  products_dict = read_dictionary('products.csv', 0)
  print (products_dict)
  with open ('request.csv', 'rt') as request_file:
    request_reader = csv.reader(request_file)
    next(request_reader)
    print("\nRequested items")
    for line in request_reader:
      product_name = products_dict[line[0]][1]
      requested_quantity = line[1]
      product_price = products_dict[line[0]][2]
      print(product_name, requested_quantity, product_price)
                                             


if __name__ == "__main__":
  main()