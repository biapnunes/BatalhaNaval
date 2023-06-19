from datetime import datetime
import time as t
import random
import Matriz as m
import AlocarNavios as a
import Arquivo as ar


def jogar(tabuleiro1,
          tabuleiro2,
          modoJogador1,
          modoJogador2,
          memoriaJogo=None):
  alfabeto = a.Alfabeto()
  pontos1 = totalPontuacao()
  pontos2 = totalPontuacao()
  turnoJogadores = 0
  memoriaJogador1 = {
    "posPrincipal": "",
    "ultiPosicao": "",
    "ultiLado": "",
    "turnos": 0
  }
  memoriaJogador2 = {
    "posPrincipal": "",
    "ultiPosicao": "",
    "ultiLado": "",
    "turnos": 0
  }
  listaCoordenada1 = []
  listaCoordenada2 = []
  data_e_hora_atuais = datetime.now()
  data_e_hora = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
  for linhas in range(1, 11):
    if memoriaJogo != None:
      tabuleiro1 = memoriaJogo['tabuleiro1']
      tabuleiro2 = memoriaJogo['tabuleiro2']
      modoJogador1 = memoriaJogo['modoJogador1']
      modoJogador2 = memoriaJogo['modoJogador2']
      listaCoordenada1 = memoriaJogo['listaCoordenada1']
      listaCoordenada2 = memoriaJogo['listaCoordenada2']
      pontos1 = memoriaJogo['pontos1']
      pontos2 = memoriaJogo['pontos2']
      memoriaJogador1["posPrincipal"] = memoriaJogo['memoriaJogador1'][
        'posPrincipal']
      memoriaJogador1["ultiPosicao"] = memoriaJogo['memoriaJogador1'][
        'ultiPosicao']
      memoriaJogador1["ultiLado"] = memoriaJogo['memoriaJogador1']['ultiLado']
      memoriaJogador1["turnos"] = memoriaJogo['memoriaJogador1']['turnos']
      memoriaJogador2["posPrincipal"] = memoriaJogo['memoriaJogador2'][
        'posPrincipal']
      memoriaJogador2["ultiPosicao"] = memoriaJogo['memoriaJogador2'][
        'ultiPosicao']
      memoriaJogador2["ultiLado"] = memoriaJogo['memoriaJogador2']['ultiLado']
      memoriaJogador2["turnos"] = memoriaJogo['memoriaJogador2']['turnos']
      turnoJogadores = memoriaJogo['turnoJogadores']
    else:
      for colunas in alfabeto:
        listaCoordenada1.append(colunas + str(linhas))
        listaCoordenada2.append(colunas + str(linhas))
  while (pontos1 != 0 and pontos2 != 0):
    if (turnoJogadores == 0):
      fraseEspera = ("Jogador 1 atacando")
      for i in range(len(fraseEspera)):
        t.sleep(0.05)
        print(fraseEspera[i], end='')
      print("\n")
      turnoJogadores, pontos2, memoriaJogador1, listaCoordenada2, tabuleiro2, estadoSaida = dispararNavio(
        turnoJogadores, pontos2, memoriaJogador1, listaCoordenada2, tabuleiro2,
        modoJogador1)
      m.MostrarTabuleiro(tabuleiro2, alfabeto, True)
    elif (turnoJogadores == 1):
      fraseEspera = ("Jogador 2 atacando")
      for i in range(len(fraseEspera)):
        t.sleep(0.05)
        print(fraseEspera[i], end='')
      print("\n")
      turnoJogadores, pontos1, memoriaJogador2, listaCoordenada1, tabuleiro1, estadoSaida = dispararNavio(
        turnoJogadores, pontos1, memoriaJogador2, listaCoordenada1, tabuleiro1,
        modoJogador2)
      m.MostrarTabuleiro(tabuleiro1, alfabeto, True)
    if estadoSaida == True:
      textoSaida()
      memoriaJogo = {
        'modoJogador1': modoJogador1,
        'modoJogador2': modoJogador2,
        'tabuleiro1': tabuleiro1,
        'tabuleiro2': tabuleiro2,
        'listaCoordenada1': listaCoordenada1,
        'listaCoordenada2': listaCoordenada2,
        'pontos1': pontos1,
        'pontos2': pontos2,
        'memoriaJogador1': memoriaJogador1,
        'memoriaJogador2': memoriaJogador2,
        'turnoJogadores': turnoJogadores,
        'data_e_hora': data_e_hora
      }
      return (memoriaJogo, estadoSaida)
  if (pontos1 == 0):
    print('***O JOGADOR 2 GANHOU!***')
    memoriaRanking = {
      'nome': 'computador',
      'turnos': memoriaJogador1["turnos"]
    }
    ar.salvarInfoArquivo(memoriaRanking, "pontuacao.txt", True)
  elif (pontos2 == 0):
    print('***O JOGADOR 1 GANHOU!***')
    nomeJogador = input('Digite o nome para salvar a pontuacao:')
    memoriaRanking = {'nome': nomeJogador, 'turnos': memoriaJogador1["turnos"]}
    ar.salvarInfoArquivo(memoriaRanking, "pontuacao.txt", True)
  print("Jogo finalizado")
  memoriaJogo = {
    'modoJogador1': modoJogador1,
    'modoJogador2': modoJogador2,
    'tabuleiro1': tabuleiro1,
    'tabuleiro2': tabuleiro2,
    'listaCoordenada1': listaCoordenada1,
    'listaCoordenada2': listaCoordenada2,
    'pontos1': pontos1,
    'pontos2': pontos2,
    'memoriaJogador1': memoriaJogador1,
    'memoriaJogador2': memoriaJogador2,
    'turnosJogadores': turnoJogadores,
    'data_e_hora': data_e_hora
  }
  return (memoriaJogo, estadoSaida)


def CoordenadaLados(JogadaAnterior, lado):
  linhaDef, colunaDef = a.pegarCoordenada(JogadaAnterior, a.Alfabeto())
  alfabetoString = "ABCDEFGHIJKLM"
  if lado == 'C':  # CIMA
    linhaDef -= 1
  elif lado == 'B':  # BAIXO
    linhaDef += 1
  elif lado == 'E':
    colunaDef -= 1
  elif lado == 'D':
    colunaDef += 1
  novaCoordenada = alfabetoString[colunaDef] + str(linhaDef + 1)

  return novaCoordenada


def escolherCoordenadaLado(Jogada, listaCoordenadas):
  listaLadoDisponivel = []
  listaLadoRealDisponivel = []
  linhaDef, colunaDef = a.pegarCoordenada(Jogada, a.Alfabeto())
  if linhaDef >= 1:  # Pode se movimentar para cima
    listaLadoDisponivel.append('C')
  if linhaDef <= 8:  # Pode se movimentar para baixo
    listaLadoDisponivel.append('B')
  if colunaDef >= 1:  # Pode se movimentar para esquerda
    listaLadoDisponivel.append('E')
  if colunaDef <= 10:  # Pode se movimentar para direita
    listaLadoDisponivel.append('D')

  for i in listaLadoDisponivel:
    coordenadaTiro = CoordenadaLados(Jogada, i)
    if (coordenadaTiro in listaCoordenadas):
      listaLadoRealDisponivel.append(i)

  return listaLadoRealDisponivel


def dispararNavio(turnoJogadores, totalTabInimigo, memoriaJogador,
                  listaCoordenadas, tabuleiroInimigo, modoJogador):
  estadoSaida = False
  alfabeto = a.Alfabeto()
  linhaDef, colunaDef = 0, 0
  coordenadaTiro = ""
  if (modoJogador == 0):  # Modo usuario
    try:
      m.MostrarTabuleiro(tabuleiroInimigo, alfabeto, True)
      print('Para encerrar o jogo digite "sair" a qualquer instante')
      coordenadaTiro = input(
        "Digite a coordenada que deseja atirar no tabuleiro inimigo=").strip(
        ).upper()
      if coordenadaTiro == 'SAIR':
        estadoSaida = True
        return (turnoJogadores, totalTabInimigo, memoriaJogador,
                listaCoordenadas, tabuleiroInimigo, estadoSaida)
      linhaDef, colunaDef = a.pegarCoordenada(coordenadaTiro, alfabeto)
    except ValueError:
      print(
        'Observaçao: A resposta deve conter letra(coluna) na primeira posicao e numero(linha) na segunda posicao!'
      )
      return turnoJogadores, totalTabInimigo, memoriaJogador, listaCoordenadas, tabuleiroInimigo, estadoSaida
    # print(f'{linhaDef+1},{colunaDef}\n')
    # print("valor no ponto:", tabuleiroInimigo[linhaDef, colunaDef])
  elif (modoJogador == 1):
    if (memoriaJogador["posPrincipal"] != ""):
      if (memoriaJogador["posPrincipal"] == memoriaJogador["ultiPosicao"]):
        listaLadoDisponivel = escolherCoordenadaLado(
          memoriaJogador["posPrincipal"], listaCoordenadas)
        if (len(listaLadoDisponivel) != 0):
          memoriaJogador["ultiLado"] = random.choice(listaLadoDisponivel)
          coordenadaTiro = CoordenadaLados(memoriaJogador["posPrincipal"],
                                           memoriaJogador["ultiLado"])
      elif (memoriaJogador["posPrincipal"] != memoriaJogador["ultiPosicao"]):
        if (memoriaJogador["ultiLado"] == "C"):
          coordenadaTiro = CoordenadaLados(memoriaJogador["ultiPosicao"], "C")
          memoriaJogador["ultiLado"] = "C"
        elif (memoriaJogador["ultiLado"] == "B"):
          coordenadaTiro = CoordenadaLados(memoriaJogador["ultiPosicao"], "B")
          memoriaJogador["ultiLado"] = "B"
        elif (memoriaJogador["ultiLado"] == "E"):
          coordenadaTiro = CoordenadaLados(memoriaJogador["ultiPosicao"], "E")
          memoriaJogador["ultiLado"] = "E"
        elif (memoriaJogador["ultiLado"] == "D"):
          coordenadaTiro = CoordenadaLados(memoriaJogador["ultiPosicao"], "D")
          memoriaJogador["ultiLado"] = "D"
        if (coordenadaTiro not in listaCoordenadas):
          listaLadoDisponivel = escolherCoordenadaLado(
            memoriaJogador["posPrincipal"], listaCoordenadas)
          if (len(listaLadoDisponivel) != 0):
            memoriaJogador["ultiLado"] = random.choice(listaLadoDisponivel)
            coordenadaTiro = CoordenadaLados(memoriaJogador["posPrincipal"],
                                             memoriaJogador["ultiLado"])
          else:
            coordenadaTiro = ""
    if (coordenadaTiro == ""):
      coordenadaTiro = random.choice(listaCoordenadas)
      memoriaJogador["posPrincipal"] = ""
      memoriaJogador["ultiPosicao"] = ""
      memoriaJogador["ultiLado"] = ""

    linhaDef, colunaDef = a.pegarCoordenada(coordenadaTiro, alfabeto)

  print("Atirando na coordenada {}\n".format(coordenadaTiro))

  # Todos
  if (coordenadaTiro in listaCoordenadas):
    memoriaJogador["turnos"] += 1
    # Não acertei o Navio
    if (tabuleiroInimigo[linhaDef][colunaDef] == "0"):
      tabuleiroInimigo[linhaDef][colunaDef] = "-"
      turnoJogadores = (turnoJogadores + 1) % 2
      if (memoriaJogador["posPrincipal"] != ""):
        memoriaJogador["ultiPosicao"] = memoriaJogador["posPrincipal"]

    # Acertei o Navio
    else:
      totalTabInimigo = totalTabInimigo - int(
        tabuleiroInimigo[linhaDef][colunaDef])
      tabuleiroInimigo[linhaDef][colunaDef] = "X"
      if (memoriaJogador["posPrincipal"] == ""):
        memoriaJogador["posPrincipal"] = coordenadaTiro
      memoriaJogador["ultiPosicao"] = coordenadaTiro
    listaCoordenadas.remove(coordenadaTiro)
    return turnoJogadores, totalTabInimigo, memoriaJogador, listaCoordenadas, tabuleiroInimigo, estadoSaida
  else:
    print("Posição ja atirada")
    return turnoJogadores, totalTabInimigo, memoriaJogador, listaCoordenadas, tabuleiroInimigo, estadoSaida


def totalPontuacao():
  tamanhoNavios, quantidadeNavios = a.caracterNavios()
  multiplicacaoNavios = 0
  for navios in range(0, len(tamanhoNavios)):
    multiplicacaoNavios += (tamanhoNavios[navios] * quantidadeNavios[navios] *
                            (navios + 1))
  return multiplicacaoNavios


def textoSaida():
  fraseSaida = 'Salvando jogo...'
  for palavra in fraseSaida:
    print(palavra, end='')
    t.sleep(0.05)
  print('\nObrigado por jogar!')
