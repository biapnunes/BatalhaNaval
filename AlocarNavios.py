import time as t
import Matriz as m
import random


def Alfabeto():  #dicionário com a representacao de colunas
  alfabeto = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11
  }
  return alfabeto


def caracterNavios():  #listas com tamanho navios e quantidade de navios
  tamanhoNavios = [5, 4, 3, 2, 1]
  quantidadeNavios = [1, 2, 2, 3, 3]
  return tamanhoNavios, quantidadeNavios


def AlocarNavios(jogador, modo):  #jogador=0 e o computador=1
  tabuleiro = m.CriarMatriz(10, 12)  # O tamanho da Matriz é um tabuleiro 10x12
  alfabeto = Alfabeto()
  tamanhoNavios, quantidadeNavios = caracterNavios()
  if modo == 0:
    print('Voce tem:\n\tNavios\t\t\t\tTotal')
    print('1 - Porta-avioes 5x1\t 1')
    print('2 - Cruzadores 4x1\t\t 2')
    print('3 - Hidroavioes 3x1\t\t 2')
    print('4 - Rebocadores 2x1\t\t 3')
    print('5 - Submarino 1x1\t\t 3')
    m.MostrarTabuleiro(tabuleiro, alfabeto,
                       False)  # mostra o tabuleiro inicialmente vazio
  for navios in range(0, 5):  # O primeiro for indica o modelo do navio
    for i in range(0, quantidadeNavios[navios]
                   ):  # O segundo for indica a quantidade de cada modelo
      achei = False
      while achei == False:
        if modo == 0:  # se o modo for igual a 0, o usuario está jogando
          try:
            listaLadoDisponivel = []
            posicaoNavios = (input(
              'Em qual posição deseja alocar o navio {} ?'.format(navios + 1))
                             ).strip().upper()
            linhaDef, colunaDef = pegarCoordenada(posicaoNavios, alfabeto)

            if tabuleiro[linhaDef, colunaDef] != '0':
              print('coordenada OCUPADA!')
              continue

            if tamanhoNavios[navios] != 1:
              listaLadoDisponivel = opcoesMovimentacao(
                linhaDef, colunaDef, tamanhoNavios, navios, tabuleiro
              )  # essa lista aponta a direcao em que os navios podem mover-se
              if len(
                  listaLadoDisponivel
              ) == 0:  # a coordenada pode estar ocupada tanto pelas verticais como horizontais
                print('Nao eh possivel alocar o navio')
                continue

            fraseLonga = ''
            for lado in listaLadoDisponivel:  # analisando os lados, é printado quais movimentos sao cabiveis pela coordenada passada
              if lado == 'B':
                fraseCurta = 'Seu navio somente pode se mover para baixo!'
                fraseLonga += 'B-PARA BAIXO\n'
              if lado == 'E':
                fraseCurta = 'Seu navio somente pode se mover para esquerda!'
                fraseLonga += 'E-PARA ESQUERDA\n'
              if lado == 'D':
                fraseCurta = 'Seu navio somente pode se mover para direita!'
                fraseLonga += 'D-PARA DIREITA\n'
              if lado == 'C':
                fraseCurta = 'Seu navio somente pode se mover para cima!'
                fraseLonga += 'C-PARA CIMA\n'
            if len(listaLadoDisponivel
                   ) == 1:  # mostra o texto em apenas uma direcao
              print(fraseCurta)
            elif len(listaLadoDisponivel) > 1:
              lado = input(fraseLonga + 'Digite a opcao=').upper().strip(
              )  # input recebe a opcao do usuario
            if tamanhoNavios[navios] != 1:
              if lado in listaLadoDisponivel:  # se o lado estiver disponivel, achei=TRUE
                achei = True  # significa que a coordenada foi preenchida
                aviso = 'Inserindo o navio no tabuleiro!'
                for palavra in aviso:
                  print(palavra, end='')
                  t.sleep(0.05)
                print('\n')
              elif lado not in listaLadoDisponivel:
                print('Lado Indisponivel!')  # senao print de aviso
                continue
            else:
              lado = None
              achei = True
          except ValueError:
            print(
              'Observaçao: A resposta deve conter letra(coluna) na primeira posicao e numero(linha) na segunda posicao!'
            )  # erro para posicaonavios recebe coordenada invalida
            continue
          m.PreencherPosicao(lado, colunaDef, tamanhoNavios[navios], tabuleiro,
                             linhaDef, navios + 1)
          m.MostrarTabuleiro(
            tabuleiro, alfabeto,
            False)  # Mostra na tela como ficou o preenchimento da posicao
        elif modo == 1:  # se modo igual a 1, significa que o computador está jogando
          aguarde = 'Aguarde o computador posicionar o navio {}'.format(
            navios + 1)
          for palavra in aguarde:
            print(palavra, end='')
            t.sleep(0.05)
          print('\n')
          linhaDef = random.randint(
            0, 9)  # sorteio de uma linha para o computador
          coluna, colunaDef = random.choice(list(
            alfabeto.items()))  # sorteio de uma coluna para o computador
          listaLadoDisponivel = opcoesMovimentacao(
            linhaDef, colunaDef, tamanhoNavios, navios, tabuleiro
          )  # retorna as opcoes de movimentacao de uma coordenada para o computador
          if listaLadoDisponivel == []:  # significa que nao ha posicao cabivel, pois está ocupada
            print('coordenada OCUPADA!')
            continue
          lado = random.choice(
            listaLadoDisponivel
          )  # sorteio do lado em que o navio do computador se movimentara
          achei = True
          m.PreencherPosicao(
            lado, colunaDef, tamanhoNavios[navios], tabuleiro, linhaDef,
            navios +
            1)  # o preenchimento da Matriz após cada parametro ser verificado

  return (tabuleiro)


def pegarCoordenada(posicaoNavios, alfabeto):  # coordenada
  if len(posicaoNavios) == 2:  # se o input receber tamanho igual a 2
    coluna = posicaoNavios[0]  # a posicao 0 representa a coluna desejada
    linha = posicaoNavios[1]  # a posicao 1 representa a linha desejada
  elif len(posicaoNavios) == 3:  # senão se o input receber tamanho igual a 3
    coluna = posicaoNavios[0]  # a posicao 0 representa a coluna desejada
    linha = posicaoNavios[1] + posicaoNavios[
      2]  # as posicoes 1 e 2 representam as linhas desejadas(numeros com mais de 1 algarismo)
  else:  # senão o input recebe informacoes inválidas
    raise ValueError  # chamamos o erro de excecao
  linhaDef = int(linha) - 1  # De 0 a 9 temos 10 linhas
  colunaDef = alfabeto[
    coluna]  # a letra desejada vai me indicar uma posicao numerica no tabuleiro que representa a coluna
  return linhaDef, colunaDef


def opcoesMovimentacao(
    linhaDef, colunaDef, tamanhoNavios, navios,
    tabuleiro):  # Mostrar Opções de movimento para cada navio
  ocupada = False
  listaLadoDisponivel = []
  distanciaColunaDireita = 12 - colunaDef  # coluna(letras) total menos a coluna(letras) desejada pelo jogador ou computador
  distanciaBaixo = 10 - linhaDef  # linha total menos a linha desejada pelo jogador ou computador
  result = 0  # o somatorio total indica uma letra ou lista de letras para a movimentacao do navio
  #if tamanhoNavios == 1:
  #  return []
  if (linhaDef + 1) >= tamanhoNavios[
      navios]:  # se linha atual for maior ou igual ao tamanho do navio, entao pode se movimentar para cima.
    for item in range(
      (linhaDef - tamanhoNavios[navios]), linhaDef
    ):  # ParaCima #inicio do range: linha desejada - tamanho do navio. #final do range: linha desejada.
      if tabuleiro[item + 1, colunaDef] != '0':
        ocupada = True
    if ocupada != True:
      result += 3
  ocupada = False
  if distanciaBaixo >= tamanhoNavios[
      navios]:  # se as linhas abaixo da coordenada(até final do tabuleiro) estiverem disponiveis em relacao ao tamanho do navio, entao pode se movimentar para baixo
    for item in range(
        linhaDef, ((linhaDef + tamanhoNavios[navios])
                   )):  # ParaBaixo #Da coordenada atual até o fim do tabuleiro
      if tabuleiro[item, colunaDef] != '0':
        ocupada = True
    if ocupada != True:
      result += 5
  ocupada = False
  if distanciaColunaDireita >= tamanhoNavios[
      navios]:  # verifica a distancia da ultima coluna até a coordenada atual
    for item in range(
        colunaDef, colunaDef + tamanhoNavios[navios]
    ):  # ParaDireita #coluna atual até a ultima coluna do tabuleiro
      if tabuleiro[linhaDef, item] != '0':
        ocupada = True
    if ocupada != True:
      result += 7
  ocupada = False
  if (colunaDef + 1) >= tamanhoNavios[
      navios]:  # a distancia da primeira coluna até a coordenada atual
    for item in range(
      (colunaDef - tamanhoNavios[navios]), colunaDef
    ):  # ParaEsquerda #inicio range: coluna-tamanho navio #final range: coluna
      if tabuleiro[linhaDef, item + 1] != '0':  # linha
        ocupada = True
    if ocupada != True:
      result += 11
  if result == 0:
    return []
  # achei = True
  if result == 3:  # cada numero primo representa uma letra para uma posicao cabivel
    listaLadoDisponivel = 'C'
  elif result == 5:
    listaLadoDisponivel = 'B'
  elif result == 7:
    listaLadoDisponivel = 'D'
  elif result == 11:
    listaLadoDisponivel = 'E'
  elif result == 8:  # cada somatorio de numeros primos representa uma lista de letras com posicoes cabiveis
    listaLadoDisponivel = ['C', 'B']
  elif result == 10:
    listaLadoDisponivel = ['C', 'D']
  elif result == 14:
    listaLadoDisponivel = ['E', 'C']
  elif result == 12:
    listaLadoDisponivel = ['B', 'D']
  elif result == 16:
    listaLadoDisponivel = ['E', 'B']
  elif result == 18:
    listaLadoDisponivel = ['E', 'D']
  elif result == 15:
    listaLadoDisponivel = ['D', 'C', 'B']
  elif result == 19:
    listaLadoDisponivel = ['E', 'C', 'B']
  elif result == 23:
    listaLadoDisponivel = ['E', 'D', 'B']
  elif result == 21:
    listaLadoDisponivel = ['E', 'D', 'C']
  elif result == 26:
    listaLadoDisponivel = ['E', 'D', 'C', 'B']
  return listaLadoDisponivel
