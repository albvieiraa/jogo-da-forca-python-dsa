import random
from os import system, name

#Função para limar a tela a cada execução
def limpar_tela():
  #windows
  if name == 'nt':
    _= system('cls')
  #Mac ou Linux
  else:
    _= system('clear')

#Função do game
def jogo():
  limpar_tela()
  print("\nBem-vindo(a) ao jogo da forca!")
  print("Adivinhe a palavra abaixo:\n")
  #lista de palavras do jogo
  palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja'] #anexar um arquivo .txt com palavras aleatórias de comidas

  #escolher a palavra aleatoriamente
  palavra = random.choice(palavras)

  #list comprehension
  letras_descobertas = ['_' for letra in palavra]

  #numero de chances
  chances = 6

  #lista para letras erradas
  letras_erradas = []

  #Loop enquanto número de chances for maior que zero
  while chances > 0:
    print(" ".join(letras_descobertas))
    print("\nChances restantes: ", chances)
    print("Letras erradas: ", " ".join(letras_erradas))

    tentativa = input("\nDigite uma letra: ").lower()
    #condicional para checar as letras corretas
    if tentativa in palavra:
      index = 0
      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[index] = letra
        index += 1
    else:
      chances -= 1
      letras_erradas.append(tentativa)
    
    #condicional quando acertar a palavra, ou seja não tem mais "_" apenas letras
    if "_" not in letras_descobertas:
      print("\nVocê venceu, a palavra era: ", palavra)
      break
  
  #condicional para avisar que as chances acabaram e o usuário perdeu o jogo
  if "_" in letras_descobertas:
    print("\nVocê perdeu, a palavra era: ", palavra)

#bloco main
if __name__ == "__main__":
  jogo()
  print("\nParabéns. Você está aprendendo programação em Python com a DSA!\n")