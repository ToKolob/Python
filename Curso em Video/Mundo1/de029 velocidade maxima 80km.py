speed_limit = 80
 
instant_speed = int(input('Qual a velocidade que o carro passou?   '))

mult = -(speed_limit - instant_speed) * 7

if instant_speed > speed_limit:
  print('multado em ' + str(mult) + 'reais')

else :
  print('velocidade dentro do limite prossiga sua viagem')