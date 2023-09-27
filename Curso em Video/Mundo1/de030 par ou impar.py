resto = ''

while resto != 99:
  number = int(input('informe um numero: '))

  resto = number%2
  if resto == 0:
    print('é um numero par')
  else: 
    print('é um numeor impar')