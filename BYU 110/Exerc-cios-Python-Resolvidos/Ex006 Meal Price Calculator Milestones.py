child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

sub_total = child_meal * child_num + adult_meal * adult_num
print (f"\nSub Total: ${sub_total:.2f} ")
