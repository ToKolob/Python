#I add .ljust and .rjust to make prices more clean to show

print ("Welcome to the Shopping Cart Program!")

item = ""
price = ""
itens = []
prices = []


valid_options = ["1","2","3","4","5"]
answer = ""
while answer not in valid_options and answer != "5":
	answer = input("\nChoose one option  \n1: Add some item to the list. \n2: remove some item. \n3: show the list. \n4: shows the total partial.\n5: show total and end the program. \n")

	if answer == "1":
		print ("Please insert your item, if you what to come back insert 'ok'.")
		item = ""
		while item != "ok":
			item = input("item: ")
			if item != "ok":
				itens.append(item)
				price = float(input("What is the price? "))
				prices.append(price)

	if answer == "3":
		print("	Shopping Card:")
		for i in range(len(itens)):
			just_price = f"{prices[i]:.2f}"
			print (f"	{i+1}.{itens[i].ljust(20)}    ${just_price}".ljust(10))
		print(f"\n	Total: ${sum(prices):.2f}")
	
	if answer == "4":
		print(f"	Total: ${sum(prices):.2f}")

	if answer == "2":
		for i in range(len(itens)):
			just_price = f"{prices[i]:.2f}"
			print (f"	{i+1}.{itens[i].ljust(20)}    ${just_price}".ljust(10))
		remove_item = int(input("which item do you what to remove? (insert the number) "))
		if remove_item > 0 and remove_item <= len(itens):
			itens.pop(remove_item-1)
			prices.pop(remove_item-1)
		print("invalid option")
		remove_item = "0"

	answer = ""
print("Thank you. Goodbye.")
