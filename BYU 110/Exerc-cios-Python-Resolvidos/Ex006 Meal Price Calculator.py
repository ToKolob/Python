child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

sub_total = child_meal * child_num + adult_meal * adult_num
print (f"\nSub Total: ${sub_total:.2f} ")

sale_taxes = tax_rate * sub_total / 100
print (f"Sales Tax: ${sale_taxes:.2f}")
total = sub_total + sale_taxes
print (f"Total: ${total:.2f}")

#To add something to the program, I put a option to pay tips.
payment = float(input("What is the payment amount? "))
tips = float(input("how much would you like to give as tips? "))
change = payment - total - tips
print (f"\nChange : ${change:.2f}")

