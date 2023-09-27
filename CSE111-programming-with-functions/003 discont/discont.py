from datetime import datetime as dt
def discont():
  weekday = dt.now().weekday()

  print('\n*** Welcome to the store ***')

  try:
    subtotal = float(input('In order to know if you are alegeble to the discont, please insert your subtotal: $'))
  except ValueError:
    subtotal = -0.000001
  
  if subtotal < 0:
    print('insert a valid number')
    subtotal = 0.000001

  elif (weekday == 1 or weekday == 2) and subtotal >= 50:
    subtotal *= 0.9
    print('Congrats, you received a discount of 10%!')

  elif(weekday == 1 or weekday == 2):
    print(f'You just need to buy more itens on the value of ${50-subtotal} to apply the discount.')

  else: 
    print('Sorry, but you are not elegeble.')

  taxes = subtotal*0.06
  print(f'Sales tax amount: ${taxes:.2f}')
  print(f'Your total is ${subtotal+taxes:.2f}.\n')

subtotal = 1
while subtotal != 0:
  discont()

