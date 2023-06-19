import pickle
import Jogar as j


def salvarInfoArquivo(memoria, caminho, ordenar):
  try:  # se o arquivo ja existe
    arquivo = open(caminho,
                   "rb")  # tenta abrir um arquivo em modo binario para leitura
    conteudo = pickle.load(arquivo)  # le o conteudo do objeto arquivo
    conteudo.append(memoria)  # acrescenta o novo ganhador
    if ordenar == True:
      conteudo = sorted(conteudo, key=lambda k: k[
        'turnos'])  # coloca os ganhadores em ordem crescente dentro do arquivo
    arquivo.close()  # fecha o arquivo
    arquivo = open(caminho, "wb")
  except Exception:  # se o arquivo nao existe, vai ser criado
    print("O arquivo foi criado")
    arquivo = open(caminho,
                   "wb")  # tenta abrir um arquivo em modo binario para escrita
    conteudo = [memoria]

  pickle.dump(conteudo, arquivo)  # Grava um dicionario no arquivo.
  arquivo.close()


def Ranking(caminho):
  # para ler o  conteudo modificado
  try:
    arquivo = open(caminho,
                   "rb")  # tenta abrir um arquivo em modo binario para leitura
    conteudo = pickle.load(
      arquivo
    )  # Ler a stream a partir do arquivo e reconstroi o objeto original.
    contador = 0
    print("\n----------------- RANKING --------------------")
    for dic in conteudo:
      contador += 1
      print("----------------------------------------------")
      print("{}° lugar - Nome:{} | Turnos:{}".format(
        contador, dic['nome'],
        dic['turnos']))  # imprime o conteúdo do dicionário
      print("----------------------------------------------")
    arquivo.close()  # fechar o arquivo# arquivo.close()
  except:
    print("Ranking vazio")


def CarregarJogo(caminho):
  try:
    arquivo = open(caminho,
                   "rb")  # tenta abrir um arquivo em modo binario para leitura
    conteudo = pickle.load(
      arquivo
    )  # Ler a stream a partir do arquivo e reconstroi o objeto original.
    print('---Jogos Salvos---')
    for item in range(len(conteudo)):
      print('jogo {} - {}'.format(item + 1, conteudo[item]['data_e_hora']))
    indiceJogo = int(input('Qual jogo deseja carregar?'))
    if indiceJogo > len(conteudo):
      print("Opcao invalida")
    else:
      tabuleiro1 = conteudo[indiceJogo - 1]['tabuleiro1']
      tabuleiro2 = conteudo[indiceJogo - 1]['tabuleiro2']
      modoJogador1 = conteudo[indiceJogo - 1]['modoJogador1']
      modoJogador2 = conteudo[indiceJogo - 1]['modoJogador2']
      j.jogar(tabuleiro1, tabuleiro2, modoJogador1, modoJogador2,
              conteudo[indiceJogo - 1])
    arquivo.close()  # fechar o arquivo

  except:
    print("Nenhum jogo salvo")
