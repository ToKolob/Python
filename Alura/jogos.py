import advinhacao
import forca
resposta = ''
resposta_valida = [1,2]
continua = '1'

while continua == '1':
  while resposta not in resposta_valida:
    print ('\nEscolha seu jogo?')
    resposta = int(input('(1)Advinhação\n(2)Forca\n...'))

  if resposta == 1:
    advinhacao.jogar()
  elif resposta == 2:
    forca.jogar()
  
  continua = input('deseja jogar outro jogo? \n(1)sim\n(2)não')
  resposta = ''