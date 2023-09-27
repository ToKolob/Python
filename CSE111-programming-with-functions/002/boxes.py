from math import ceil as c


items = int(input('\nEnter the number of items: '))
capacity = int(input('Number of items pack per box: '))
boxes = c(items/capacity)
print(f'Has to be {boxes} boxes to pack the items\n')

