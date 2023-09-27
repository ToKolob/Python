from datetime import datetime
import math as mt

def tire_volume():
  width_of_the_tire = float(input('\nEnter the width of the tire in mm  '))
  aspect_ratio_of_the_tire = float(input('Enter the aspect ratio of the tire  '))
  diameter_of_the_wheel = float(input('Enter the diameter of the wheel in inches  '))
  pi = mt.pi
  volume_of_the_tire = (pi*(width_of_the_tire**2)*aspect_ratio_of_the_tire*(width_of_the_tire*aspect_ratio_of_the_tire+2540*diameter_of_the_wheel))/(10**10)
  current_date_and_time = datetime.now()



  user_data = (f"{current_date_and_time:%Y-%m-%d}, width of the tire:{width_of_the_tire}, aspect ratio of the tire:{aspect_ratio_of_the_tire}, diameter of the wheel:{diameter_of_the_wheel}, volume of the tire:{volume_of_the_tire:.2f} ")

  print (f'\nThe approximate volume is {volume_of_the_tire:.2f} liters\n')

  with open("volumes.txt", mode='at') as volumes:
    volumes.write('\n'+ user_data)

  has_interest = input('Has interest in buy the tire? (y/n )')
  if has_interest == 'y':
    phone_number = input('Please enter your phone number: ')
    with open("volumes.txt", mode='at') as volumes:
      volumes.write(f', phone:{phone_number}.' )
    print('Our specialist will contact you soon!')


while True:
  tire_volume()