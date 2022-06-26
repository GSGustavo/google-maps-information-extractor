import maps
import actions
from selenium import webdriver
from help import *
from os.path import isfile
from pyautogui import hotkey


# from selenium.webdriver.common.by import By


def limpar():
    # print('limpa')
    hotkey("ctrl", 'l')


# Opção 1
listaNumerosCidades = list()

cidades = ["Campos de Júlio - MT",
           "Salto do Céu - MT"]

cidadesValues = {"Campos de Júlio - MT": 9,
                 "Salto do Céu - MT": 11}

cidadesAr = cidades[:]  # Mostrar para o usuário que a cidade que ele escolheu foi retirada
cidadesAdicionar = list()  # <<<<<<<<<<<<<<< E adicionada aqui
# Opção 1

# Escolha de Categorias
ct = [['Supermercados', 'Mercados'], 'Oficinas', 'Restaurantes', 'Lanchonetes', 'Informática e Eletrônicos',
      'Eletrodomésticos', 'Roupas e Vestuário', 'Papelarias', 'Gráficas', 'Serviços de Internet', 'Farmácias',
      'Hotéis']

ctPersonalizar = ['Supermercados', 'Mercados', 'Oficinas', 'Restaurantes', 'Lanchonetes', 'Informática e Eletrônicos',
                  'Eletrodomésticos', 'Roupas e Vestuário', 'Papelarias', 'Gráficas', 'Serviços de Internet',
                  'Farmácias', 'Hotéis']

'''for item in ct:
    if isinstance(item, list):
        for i in item:
            ctPersonalizar.append(i)
    else:
        ctPersonalizar.append(item)'''

ctAr = ctPersonalizar[:]
ctAdicionar = list()

# ct ctAr ctAdicionar

# Escolha de Categorias

# cidades = []

# Opção 2
arquivosTxt = dict()
arquivosTxtArAd = list()
# Opção 2

for i in range(len(cidades)):
    listaNumerosCidades.append(i)

if len(cidades) == 0:
    print("Sem cidades!")
    quit()

escolheu = False
totLinhas = 0
encontrouTxt = False  # Ter essa verificação para a opção 2

for cidade in listaNumerosCidades:

    if isfile(f'{cidades[cidade]}.txt'):
        arquivo = open(f'{cidades[cidade]}.txt', 'r', encoding='utf-8')
        totLinhas = len(arquivo.readlines())

        arquivosTxt[cidade] = [cidades[cidade], totLinhas]  # Adicionando as

        arquivo.close()
        encontrouTxt = True

# Opção 2
auxTxt = list()

for item in arquivosTxt.values():
    auxTxt.append(item[0])
    print(item[0])
arquivosTxtAr = auxTxt[:]
# Opção 2

# ===============================================
voltar = False
opCat = 2
while True:
    ctAr = ctPersonalizar[:]
    cidadesAr = cidades[:]
    limpar()
    title("Web Scraping - Extração de Dados")

    title("Cidades que estão cadastradas")
    for cidade in range(len(cidades)):
        print(f"  > {cidades[cidade]}")  # print(f"[{cidade}] - {cidades[cidade]}")

    title("Arquivos .txt Encontrados")
    for cidade in range(len(arquivosTxt)):
        print(f"  > {arquivosTxt[cidade][0]}.txt | Linhas: {arquivosTxt[cidade][1]} | Empresas: "
              f"{arquivosTxt[cidade][1] / 6}")
        # print(f"[{cidade}] - {arquivosTxt[cidade][0]}.txt | Linhas: {arquivosTxt[cidade][1]} | Empresas: "
        #               f"{arquivosTxt[cidade][1] / 6}")
    if not encontrouTxt:
        error_controlled("Não foram encontrados Arquivos .txt com dados")

    # ===============================================
    sep()
    while True:
        pergunta = verify_int('''O que você quer fazer?
  [1] - Buscar empresas no Google Maps e criar o .txt
  [2] - Cadastrar empresas do .txt na Localizar Fácil
  [3] - Buscar e Cadastrar empresas
  [4] - Apagar empresas
  [5] - Editar Empresas
  [99] - Sair
Opção: ''')
        listaNunsOps = range(1, 6)
        if pergunta not in listaNunsOps and pergunta != 99:
            error_controlled(f'Por favor, insira um valor válido {listaNunsOps}')
        else:
            break


    def putAndDelete(ar, ad, geral, titlee, subtitle):
        """
        Função geral para utilizar quando é preciso perguntar ao usuário quais valores ele quer selecionar.
        Essa função ajuda a ter um maior controle dos valores!

        :param ar: É a cópia da lista geral, é usado para retirar os valores que foram selecionados pelo usuário
        :param ad: Os valores que são selecionados pelo usuário vem para cá
        :param geral: Lista Geral com os valores predefinidos la em cima
        :param titlee: Título da função
        :param subtitle: Subtitulo da função
        :return: False ou True
        """
        aux = list()
        # op = 0
        if isinstance(geral, dict):
            for item in geral.values():
                aux.append(item[0])
                print(item[0])
            geral = aux
        while len(ar) > 0:
            limpar()
            title(titlee)  # title
            print(subtitle)  # subtitle

            for item in range(len(ar)):
                print(f"  [{item}] - {ar[item]}")
            sep()

            print("[99] - Voltar")
            print("[100] - Não quero adicionar mais nada")
            op = verify_int("Opção: ")
            if op not in range(len(ar)) and op not in [99, 100]:  # Verificando a resposta
                error_controlled("Por favor, selecione o número dos itens listadas apenas!")
            elif op == 99:
                ad.clear()
                ar.clear()
                ar = geral[:]  # Resetar a lista de itens pq o usuário clicou em voltar para o menu
                voltar = True
                print(ar)
                return voltar
            elif op == 100:
                if len(ad) == 0:
                    error_controlled("Você não pode continuar com o programa pois não selecionou nenhum item")
                else:
                    break
            else:
                ad.append(ar[op])
                # print(cidadesAdicionar)
                ar.remove(ar[op])

        if len(ar) == 0:
            return False


    def opUm(opcao):
        if opcao == 0:
            put = 'Buscar empresas no Google Maps'
        else:
            put = 'Buscar e Cadastrar Empresas'
        sep()
        while True:
            limpar()
            opCat = verify_int("Você quer personalizar as categorias a serem buscadas? [1 = Não / 0 = Sim] ")
            if opCat not in [0, 1]:
                error_controlled("Por favor insira apenas 0 ou 1!")
                continue
            else:
                if opCat == 0:
                    result = putAndDelete(ctAr,
                                          ctAdicionar,
                                          ctPersonalizar,
                                          "Seleção de Categorias",
                                          "Selecione as categorias que deseja buscar")
                    if result:
                        return result
                break
        return [putAndDelete(cidadesAr,
                             cidadesAdicionar,
                             cidades,
                             put,
                             "Escolha as cidades que queira deixar automaticamente rodando"), opCat]


    def opDois():
        if len(arquivosTxtAr) != 0:  # Verificando se la em cima o programa achou algum arquivo
            return putAndDelete(arquivosTxtAr,
                                arquivosTxtArAd,
                                arquivosTxt,
                                'Cadastrar empresas na Localizar Fácil',
                                "Escolha as cidades que queira deixar automaticamente rodando")
        else:
            return 2


    def deletar(i, f, n):
        actions.deletar(i, f, n)


    colocarAqui = 0
    listaResultados = list()
    if pergunta == 1:
        colocarAqui = 0
    elif pergunta == 3:
        colocarAqui = 1
    if pergunta in [1, 3]:
        listaResultados = opUm(colocarAqui)

    if pergunta in [1, 3]:
        if isinstance(listaResultados, list):
            if listaResultados[0]:  # Esse if é porque a função retorna o "voltar" como false ou true
                continue
        elif listaResultados:
            # Resetando o cacete das listas
            continue
    elif pergunta == 2:
        instancia = opDois()
        if instancia:
            continue
        # Esse if é porque a função retorna o "voltar" como false ou true
        elif instancia == 2:
            error_controlled("Não foram encontrados arquivos para cadastrar!")
            continue

    elif pergunta == 4:
        sairOpcoesDelete = False
        while True:
            limpar()
            title("Apagar Empresas em Massa")
            print("OBS: O intervalo entre os dois valores precisa ser maior ou igual que 10!")
            inicio = verify_int("Digite o id inicial: ")
            fim = verify_int("Digite o id final: ")
            if inicio > fim or (inicio < 1 and fim < 1) or (fim - inicio < 10):
                error_controlled('''Possíveis erros:
  [1] - O valor inicial está maior que o valor final
  [2] - Alguns dos valores estão negativos
  [3] - O intervalo entre os valores é menor que 10''')
                print(f"Valor inicial: {inicio}")
                print(f"Valor final: {fim}")
                continue
            print("Escolha uma das opções")
            while True:
                # opcao = verify_int(f"Quer apagar as empresas de {inicio} até {fim}? ")
                print(f'''[1] - Seguir e deletar empresas de {inicio} até {fim}
  [2] - Digitar os valores novamente
  [3] - Voltar para o menu principal''')
                opcao = verify_int("Opção: ")
                if opcao not in range(1, 4):
                    error_controlled("Digite apenas os valores apresentados!!")
                else:
                    break
            if opcao in [1, 3]:
                if opcao == 3:
                    sairOpcoesDelete = True
                break
            else:
                continue
        if sairOpcoesDelete:
            continue
    sep()

    # quit()  # Ativar apenas para testar o menu

    if pergunta != 99:
        navegador = webdriver.Chrome()
        navegador.maximize_window()
    if pergunta in [1, 3]:
        if listaResultados[1] == 1:
            ctAdicionar = ct[:]


    def escreva(ic):
        file = open(f'{cidades[cidades.index(ic)]}.txt', 'w', encoding='utf-8')
        # ===============================================

        maps.escrever(navegador, cidades[cidades.index(ic)], file, ctAdicionar)
        # ===============================================


    def todos(modo):
        if modo in [1, 3]:
            forIn = cidadesAdicionar
        elif modo == 4:
            deletar(inicio, fim, navegador)
            forIn = arquivosTxtArAd  # Não vai ser usado, é só pro pycharm parar de reclamar!
        else:
            forIn = arquivosTxtArAd
        for indiceCidade in forIn:  # range(len(cidades))
            idc = cidades[cidades.index(indiceCidade)]
            if modo == 1:
                # ct ctAr ctAdicionar
                escreva(indiceCidade)
            elif modo == 2:
                actions.adicionar(navegador, idc, cidadesValues[idc])
            elif modo == 3:
                escreva(indiceCidade)
                actions.adicionar(navegador, idc, cidadesValues[idc])


    if pergunta == 1:
        print(f'Cidades para escrever no txt: {cidadesAdicionar}')
        print(f"Com as categorias: {ctAdicionar}")
        todos(1)
    elif pergunta == 2:
        print(f'Cidades para adicionar na Localizar Fácil: {arquivosTxtArAd}')
        todos(2)

    elif pergunta == 3:
        print(f'Cidades para escrever no txt e adicionar na Localizar Fácil: {cidadesAdicionar}')
        print(f"Com as categorias: {ctAdicionar}")
        todos(3)
    elif pergunta == 4:
        todos(4)
    break
