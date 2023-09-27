def jogar():

  arquivo = open("c:\Users\lucas\Documents\Programação\Estudos\Python\Alura\palavras.txt", "r")

  palavra_secreta = 'Moroni'
  letra_chutada = []
  tentativa = ''

  def dica():
    print('Sua dica é: ',end='')
    for letra in palavra_secreta:  

      if letra.lower() in letra_chutada:
        print (letra,end=' ')
      else:
        print ('_',end=' ')
      
    print(f'\n Você ja tentou {letra_chutada}')

    
        
    

  while tentativa.lower() != palavra_secreta.lower():
    dica()
    tentativa = input('Informe uma letra ou a palavra secreta')
    if len(tentativa) > 1:

      print(f'Você informou a palavra {tentativa}')    

      if tentativa.lower() == palavra_secreta.lower():
        print ('Parabéns você acertou!')
        break
      else:
        print ('você errou!')
    else:

      letra = tentativa.lower()
      letra_chutada.append(letra)
    
      

if __name__ == '__main__':
  jogar()