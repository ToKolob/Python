from formula import parse_formula

def main():
    # Get a chemical formula for a molecule from the user.
  sample_chemical_formula = input('Please, insert a chemical formula of the sample. ')

    # Get the mass of a chemical sample in grams from the user.
  sample_mass = float(input('Please, insert the mass of the sample. '))

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
  periodic_table = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
  sample_parse_formula = parse_formula(sample_chemical_formula,periodic_table)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
  sample_molar_mass = compute_molar_mass(sample_parse_formula,periodic_table)

    # Compute the number of moles in the sample.
  sample_n_moles = sample_mass/sample_molar_mass

    # Print the molar mass.
  print (f"{sample_molar_mass:.5f} grams/mole ")

    # Print the number of moles.
  print (f"{sample_n_moles:.5f} moles")


  
  

def make_periodic_table():
  lines = []
  with open ("data.txt","r") as raw_data:
    raw_lines = raw_data.readlines()
    for raw_line in raw_lines:
      raw_line = raw_line.replace('"', '').replace(",", "")
      line = raw_line.split()
      try:
        line = [line[0], line[1], float(line[2])]
      except:
        continue
      lines.append(line)

      #transform the list into a dictionary
  periodic_table = {
    line[0]: [line[1], line[2]] for line in lines

  }
  return periodic_table

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    total_molar_mass = 0
    for list in symbol_quantity_list:
      symbol, quantity = list
      atomic_mass = periodic_table_dict[symbol][1]
      total_molar_mass += float(atomic_mass) * quantity


    # Return the total molar mass.
    return total_molar_mass



if __name__ == "__main__":
  main()