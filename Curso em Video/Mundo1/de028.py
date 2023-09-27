#elementos predecessores
import random as rd

randNum = rd.randint(0,5)

tryNum = ''

validAnswers = [0,1,2,3,4,5]

#elementos centrais


while tryNum != randNum:
  while tryNum not in validAnswers:
    tryNum = int(input('escolha um numero de 0 a 5:    ') or '10')

  if tryNum == randNum:
    print ('você acertou')
    break

  else:
    print ('Errou, tente novamente')
  
  tryNum =''


