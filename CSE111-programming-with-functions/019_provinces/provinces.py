list = []
with open ('provinces.txt', 'rt') as provinces:
  for line in provinces:
    list.append(line.strip())

print(list)

list.pop(0)

print()

print(list)

list.pop(-1)

print()

print(list)

print()

list_replaced = []
ab_count = 0
for line in list:
  if line != "AB":
    list_replaced.append(line)
  else:
    ab_count += 1
list = list_replaced

    
print(list)
print(ab_count)

