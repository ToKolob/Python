first_name = input('What is your first name?')
last_name = input('What is your last name?')
print(f'\nYour name is {last_name.capitalize()}, {first_name.capitalize()} {last_name.capitalize()}.')


print('Please enter the following information:\n')
first_name = input('First name: ')
last_name = input('Last name: ')
Email = input('Email eddress: ')
Phone = input('Phone number: ')
Job = input('Job title: ')
ID = input('ID Number: ')
print('\nThe ID CArd is: \n----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()} \n{Job.title()} \n{ID} \n\n{Email}\n{Phone} \n----------------------------------------')
