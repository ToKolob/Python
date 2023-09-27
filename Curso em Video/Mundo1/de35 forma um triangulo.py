while 1 != 2:
  arrow1 = int(input('Informe a 1 reta: ') or 0)
  arrow2 = int(input('Informe a 2 reta: ') or 0)
  arrow3 = int(input('Informe a 3 reta: ') or 0)

  arrows = [arrow1,arrow2,arrow3]

  biggest = 0
  the_rest = 0

  for arrow in arrows:
    if arrow > biggest:
      biggest = arrow
    else:
      the_rest += arrow

  if the_rest > biggest:
    print('forma um triangulo \n')

  else:
    print('não forma triangulo \n')


