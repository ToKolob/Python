#How old are you? 25
#On your next birthday, you will be 26

#How many egg cartons do you have? 3
#You have 36 eggs

#How many cookies do you have? 18
#How many people are there? 8
#Each person may have 2.25 cookies

age = input('How old are you? ')
print(f'On your next birthday You will be {(int(age))+1} years old')
print()
egs = input('How many egg cartons do you have? ')
print (f'Then you have {(int(egs))*12} egs')
print()
cookies = input('How many cookies do you have? ')
people = input('How many peaple are there? ')
print(f'Each person may have {(float(cookies))/float(people)} cookies')