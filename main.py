import AlocarNavios as a
import Jogar as j
import Arquivo as ar


def Menu():
  resposta = 1
  while resposta != 6:
    print('*Batalha Naval*')
    print('Menu:')
    print('1 - Jogar contra o computador')
    print('2 - Jogar contra outro usuario')
    print('3 - Ver pontuação atual')
    print('4 - Carregar um jogo')
    print('5 - Apagar todos os jogo salvos')
    print('6 - Sair do jogo')
    try:
      resposta = (int(input('digite sua escolha=')))
      if resposta == 1:
        tabuleiro1 = a.AlocarNavios(0, 0)
        tabuleiro2 = a.AlocarNavios(1, 1)
        memoriaJogo, estadoSaida = j.jogar(tabuleiro1, tabuleiro2, 0, 1)
        if estadoSaida == True:
          ar.salvarInfoArquivo(memoriaJogo, 'rest.txt', False)
      elif resposta == 2:
        tabuleiro1 = a.AlocarNavios(0, 0)
        tabuleiro2 = a.AlocarNavios(0, 0)
        memoriaJogo, estadoSaida = j.jogar(tabuleiro1, tabuleiro2, 0, 0)
        if estadoSaida == True:
          ar.salvarInfoArquivo(memoriaJogo, 'rest.txt', False)
      elif resposta == 3:
        ar.Ranking('pontuacao.txt')
      elif resposta == 4:
        ar.CarregarJogo('rest.txt')
      elif resposta == 5:
        arquivo = open("rest.txt", "w")
        print("Todos os jogos foram apagados.")
        arquivo.close()
      elif resposta == 6:
        print('Finalizando Jogo!')
    except ValueError:
      print('OPCAO INVALIDA!')


Menu()
