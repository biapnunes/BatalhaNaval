import numpy as np


def CriarMatriz(linha, coluna):
  matriz = linha, coluna
  tabuleiro = np.full(matriz, 0, dtype=str)
  return (tabuleiro)


def MostrarTabuleiro(tabuleiro, alfabeto, modoNavios):
  print('\t\t---TABULEIRO---\n')
  print('\t', end='')
  for letras in alfabeto:
    print(letras, end=' ')
  contadorLinha = 1
  contadorColuna = 1
  for linha in tabuleiro:
    print('\t')
    print(contadorLinha, '\t', end='')
    contadorLinha += 1
    for coluna in linha:
      if modoNavios == True and coluna != 'X' and coluna != '-':
        print(('0'), end=' ')
      else:
        print((coluna), end=' ')
      contadorColuna += 1
  print('\n')


def PreencherPosicao(lado, colunaDef, tamanhoNavios, tabuleiro, linhaDef,
                     navios):
  if lado == 'C':
    for item in range((linhaDef - tamanhoNavios), linhaDef):  # ParaCima
      tabuleiro[item + 1, colunaDef] = navios
  elif lado == 'B':
    for item in range(linhaDef, ((linhaDef + tamanhoNavios))):  # ParaBaixo
      tabuleiro[item, colunaDef] = navios
  elif lado == 'D':
    for item in range(colunaDef, colunaDef + tamanhoNavios):  # ParaDireita
      tabuleiro[linhaDef, item] = navios
  elif lado == 'E':
    for item in range((colunaDef - tamanhoNavios), colunaDef):  # ParaEsquerda
      tabuleiro[linhaDef, item + 1] = navios
  elif tamanhoNavios == 1:  # Submarino
    tabuleiro[linhaDef, colunaDef] = navios
