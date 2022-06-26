from selenium.webdriver.common.by import By
from time import sleep
# import pyautogui
from selenium.common.exceptions import *


cidades = ["Araputanga - MT", "Cáceres - MT", "Pontes e Lacerda - MT"]

categorias = {  # Plural - 12
    'Supermercados': ['Supermercado', 'Mercado', 'Mercearia', 'Supermercado de descontos',
                      'Mercado de produtos agrícolas', 'Loja de Conveniência', 'Distribuidora de Bebidas',
                      'Fornecedor de produtos alimentícios', 'Distribuidora de Bebidas', 'Doceria', 'Padaria'],
    'Oficinas': ['Oficina mecânica', 'Mecânica para carros', 'Oficina mecânica de motos', 'Oficina de caminhões',
                 'Autoelétrico', 'Loja de autopeças', 'Autoelétrica', 'Loja de peças para motocicletas',
                 'Loja de Material Hidráulico', 'Fabricante de peças de máquinas',
                 'Manutenção de Máquinas Industriais', 'Posto de combustível'],
    'Restaurantes': ['Restaurante', 'Pizzaria', 'Bar', 'Açougue', 'Padaria', 'Sorveteria', 'Supermercado',
                     'Churrascaria', 'Hamburgueria', 'Restaurante Chinês', 'Loja de comidas Naturais'],
    'Lanchonetes': ['Lanchonete', 'Café', 'Confeitaria'],  # Restaurantes e Lanchonetes, mesmas palavras chaves
    'Informática e Eletrônicos': ['Loja de eletrônicos', 'Assistência Técnica de Informática',
                                  'Serviço de informática', 'Loja de Informática',
                                  'Oficina de consertos de eletrônicos'],
    'Eletrodomésticos': ['Loja de eletrônicos', 'Loja de Conveniência', 'Loja de eletrodomésticos',
                         'Fornecedor de peças para eletrodomésticos', 'Loja de móveis usados', 'Loja'],
    'Roupas': ['Loja de moda feminina', 'Loja de moda masculina', 'Loja de Roupa', 'Loja de vestidos', 'Confecção',
               'Loja de departamento', 'Loja de moda infantil', 'Loja de roupas de trabalho'],
    'Papelarias': ['Loja de variedades', 'Papelaria'],
    'Gráficas': ['Gráfica', 'Designer Gráfico'],  # Papelaria e Grafica
    'Serviços de Internet': ['Consultoria de informática', 'Operadora de internet', 'Agência de marketing digital',
                             'Webdesigner, Agência de publicidade', 'Empresa de Software', 'Serviço de informática',
                             'Empresa de telecomunicação'],
    'Farmácias': ['Drogaria', 'Loja de produtos naturais', 'Farmácia', 'Farmácia de homeopatia',
                  'Loja de Artigos Hospitalares'],
    'Hotéis': "0"
}

# ======================================
oldCt = [['Supermercados', 'Mercados'], 'Oficinas', 'Restaurantes', 'Lanchonetes', 'Informática e Eletrônicos',
         'Eletrodomésticos', 'Roupas e Vestuário', 'Papelarias', 'Gráficas', 'Serviços de Internet', 'Farmácias',
         'Hotéis']
# ======================================

palavrasChave = {"Supermercados": "Mercados, Produtos, Alimentos, Bebidas",
                 "Oficinas": "Mecânicas, Auto, Oficinas, Auto Center, Auto Peças",
                 "Restaurantes": "Comidas, Bebidas, Lanchonetes, Restaurantes, Lanches",
                 "Informática e Eletrônicos": "Informática, Computadores, Eletrônicos, Técnicos, Técnicas",
                 "Eletrodomésticos": "Eletrodomesticos, Eletronicos, Móveis, Varejos, Aparelhos",
                 "Roupas": "Roupas, Vestuarios, Masculinos, Femininos, Calças, Camisetas, Shorts",
                 "Papelarias": "Papelarias, Lapis, Canetas, Folhas, Impressões",
                 "Serviços de Internet": "Internet, Serviços de Internet, Provedores",
                 "Farmácias": "Drogarias, Farmácias, Remédios",
                 "Hotéis": "Hotéis, Hotelarias, Pousadas"}

descartados = list()  # Categorias que não foram achadas nas listas acima
empresas = list()
classEmpresaZero = "hfpxzc"
nomesEmpresas = list()


def zoomOut(navegador):
    # navegador.execute_script("document.body.style.zoom = 0.8")
    print('')


def proxima(b1, n):
    count = 0
    soUmaPagina = False

    while True:
        print("ABC")
        paginaBrancaBaitOuCidade = False
        disable = False

        textoPageVazia = n.find_elements(By.CLASS_NAME, "qBF1Pd")
        if len(textoPageVazia) == 0:
            break

        try:

            disable = b1.get_attribute("disabled")
            print('Ele tenta achar o botao')
            print(disable)
        except StaleElementReferenceException:
            count -= 1
            paginaBrancaBaitOuCidade = True
            print('--->>>>>>>>>>>>>>>>>> NÃO')

        contarclickproxima = 0

        if paginaBrancaBaitOuCidade:
            break
        if disable is None:
            while True:
                print('POIK')
                if contarclickproxima == 2:
                    break
                try:
                    b1.click()
                    break
                except (ElementClickInterceptedException, ElementNotInteractableException) as erro:
                    contarclickproxima += 1
                    print(f'TENTATIVAS DE CLIQUES: {contarclickproxima}')
                    print(erro)
            sleep(1.5)
            textoPageVazia = n.find_elements(By.CLASS_NAME, "njRcn")

            print(f'textoPageVazia >>>>>>>>>>>> {len(textoPageVazia)}')

            if len(textoPageVazia) >= 1:
                break
            count += 1
            sleep(1.5)
        else:
            break
    if count == 0:
        print(f'!!!!!!!!!!!!!!!!!!! ENTROU EM COUNT == 0')
        count = 1
        soUmaPagina = True
    return [count, soUmaPagina]


def procuraBtnProx(n):
    prox = ''
    achou = False
    btnProxBug = 0
    while True:
        print("CBA")
        if btnProxBug == 5:
            break
        try:
            prox = n.find_element(By.ID, "ppdPk-Ej1Yeb-LgbsSe-tJiF1e")
            achou = True
            break
        except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException) as erro:
            print(erro)
            btnProxBug += 1
            # n.refresh()
            sleep(2)
            continue
    if achou:
        return prox
    else:
        return 0


def focar(val, n):
    tentativa = 0
    script = f'document.getElementsByClassName("Dzbife")[{val}].focus()'
    while True:
        print("While 1")
        tentativa += 1
        try:
            n.execute_script(script)
            break
        except JavascriptException as erro:  # ENTRA EM LOOPING INFINITO
            print(erro)
            if tentativa == 10:
                break
            continue


def pesquisar(valorPesquisar, elementS, btnS):
    while True:
        print("MNB")
        try:
            elementS.clear()
            elementS.send_keys(f'{valorPesquisar}')
            btnS.click()
            break
        except (ElementNotInteractableException, InvalidElementStateException, NoSuchElementException) as erro:
            print(erro)
            sleep(2)
            pass


def carregarInformacoes(nav):
    while True:
        try:
            nav.execute_script('''painel = document.getElementsByClassName("Yr7JMd-pane-content")
    tam = painel[4].scrollHeight
    painel[4].scrollTo(0, 750)''')
            break
        except JavascriptException:
            pass


def fecharCard(navegador):
    # Fechar o card da empresa depois de extrair as informações
    sair = 0
    while True:
        print('KBXTY')
        try:
            if sair == 5:
                break
            exitCard = navegador.find_elements(By.CLASS_NAME, 'VfPpkd-icon-LgbsSe')
            exitCard[0].click()
            #  Botão para fechar o card da empresa, pois ele estava bugando
            break
        except:
            sair += 1
            pass

def miniMapa(navegador):
    parar = 0
    while True:
        try:
            minimapa = navegador.find_elements(By.CLASS_NAME, 'yHc72')
            minimapa[1].click()
            break
        except:
            parar += 1
            pass

def extrair(cat, loc, cid, filePara, nave, catct, ctsing):
    def chamar(c, lc, cd, fileP, navegador, ct, categoriasSing):
        try:
            navegador.implicitly_wait(2)
        except InvalidSessionIdException:
            pass
        sleep(2)

        while True:
            print("AÇMXZ")
            try:
                search = navegador.find_element(By.ID, "searchboxinput")
                break
            except InvalidSessionIdException:
                sleep(3)
                pass

        while True:
            print("AÇMXZ")
            try:
                search_btn = navegador.find_element(By.ID, "searchbox-searchbutton")
                break
            except InvalidSessionIdException:
                sleep(3)
                pass

        termos = [f'Cidade de {cd}', f'{c} na cidade de {cd}']

        for termo in termos:
            while True:
                print('PSQWLH')
                try:
                    pesquisar(termo, search, search_btn)
                    zoomOut(navegador)
                    break
                except InvalidSessionIdException:
                    pass
            sleep(2)

        print(f'{c} em {cd}')

        empresa = list()
        sleep(3)

        px = procuraBtnProx(navegador)

        resultsProx = proxima(px, navegador)  # Retorna os resultados depois de ver quantas paginas tem
        count = resultsProx[0]
        if not resultsProx[1]:
            count += 1
        print(f'Páginas: {count}')  # Paginas
        navegador.refresh()
        sleep(2)

        def getInfos(fp=None):
            sleep(1.5)
            # Nome
            print(navegador.current_url)
            nome = navegador.title
            nome = nome[:-14]
            print(nome)
            if len(nome.split()) == 1:
                print('Nome == 1')
                empresa.clear()
                return 0

            if nome in nomesEmpresas:
                empresa.clear()
                print("Nome")
                return 0
            else:
                sleep(1)
                empresa.append(nome)
                nomesEmpresas.append(nome)

            # Endereço
            if c == "Hotéis":
                carregarInformacoes(navegador)
            # info = navegador.find_elements(By.CLASS_NAME, "QSFF4-text")

            tentativa = 0
            enderecoTexto = ''
            print(enderecoTexto)
            info = navegador.find_elements(By.CLASS_NAME, "Io6YTe")
            while True:

                print('OPH')
                # sleep(0)
                tentativa += 1
                if tentativa == 10:
                    return 0
                try:
                    enderecoTexto = info[0].text
                    print(info[0].text)
                    break
                except IndexError as erro:
                    sleep(1)
                    print(erro)
                    pass

            print(f'Endereço captado: {enderecoTexto}')
            # print(f'Cidade: {cd}')
            print(f'Endereço de outra forma: {info[0].text}')

            if cd in info[0].text:
                if "Unnamed Road" in enderecoTexto:
                    endere = enderecoTexto.split()
                    enderecoTexto = ''
                    for v in range(2):
                        if v == 0:
                            usarP = "Unnamed"
                        else:
                            usarP = "Road"
                        for palavra in endere:
                            if palavra == usarP:
                                endere.remove(palavra)
                    for palavra in endere:
                        enderecoTexto += f"{palavra} "
                empresa.append(enderecoTexto)
            else:
                empresa.clear()
                print("PRNEND")
                return 0

            # Telefone
            # info = navegador.find_elements(By.CLASS_NAME, "QSFF4-text")
            naoConseguiu = True
            for v in range(1, len(info)):
                content = info[v].get_attribute('innerHTML')
                if len(content) != 0:
                    contentZero = content[0]
                    if contentZero == "(":
                        empresa.append(info[v].get_attribute('innerHTML'))
                        naoConseguiu = False
                        break
            if naoConseguiu:
                empresa.append('0')

            infoCategoria = navegador.find_elements(By.CLASS_NAME, "DkEaL")  # Yr7JMd-pane-hSRGPd

            # Categoria
            if cat != "Hotéis":
                naoEncontrouCategoria = True
                for v in range(len(infoCategoria)):
                    ci = infoCategoria[v].text
                    print(ci)

                    procuraLa = lc
                    if lc == "Roupas e Vestuário":
                        procuraLa = "Roupas"
                    elif lc in ['Supermercados', 'Mercados']:
                        procuraLa = 'Supermercados'

                    if "avaliações" not in ci and 'avaliação' not in ci and ci != "" and ci in categorias[procuraLa]:
                        if lc in ['Supermercados', 'Mercados']:
                            empresa.append("Supermercados")
                        elif lc == "Roupas e Vestuário":
                            empresa.append("Vestuário")
                        else:
                            empresa.append(categoriasSing[ct.index(procuraLa)])
                        naoEncontrouCategoria = False
                        break
                    else:
                        if 'avaliações' not in ci and 'avaliação' not in ci and ci != '':
                            descartados.append(ci)

                if naoEncontrouCategoria:
                    print("Categoria")
                    empresa.clear()
                    return 0

            else:  # elif cat == "Hotéis":
                empresa.append("Hotéis")

            while True:
                print('PCH')
                try:
                    if lc == "Lanchonetes":
                        empresa.append(palavrasChave["Restaurantes"])
                    elif lc == "Gráficas":
                        empresa.append(palavrasChave["Papelarias"])
                    elif lc == "Roupas e Vestuário":
                        empresa.append(palavrasChave["Roupas"])
                    elif lc == 'Mercados':
                        empresa.append(palavrasChave["Supermercados"])
                    else:
                        empresa.append(palavrasChave[lc])
                    break
                except KeyError as erro:
                    print(erro)
                    empresa.append('Empresa, Localizar Fácil')
                    break

            # Link Google Maps
            empresa.append(nome + ' - ' + enderecoTexto)
            print(empresa)
            for informacao in empresa:
                fp.write(f"{informacao}\n")
            print("Append")
            empresa.clear()

            # IMPORTANTE

        def desca():
            historico = list()

            def descer(cez):
                sleep(0.2)
                empresaNaPagina = navegador.find_elements(By.CLASS_NAME, cez)
                quant = len(empresaNaPagina)
                historico.append(quant)
                script = 'document.getElementsByClassName("hfpxzc")'
                navegador.execute_script(f'{script}[{quant - 1}].focus()')

                if historico.count(quant) == 1:
                    descer(classEmpresaZero)
                return quant

            descer(classEmpresaZero)

            return max(historico)

        def clicarEmpresas(quantidadeEmpresasNaPagina, tipo):
            while True:
                print("HJB")
                print(f'quantidadeEmpresasNaPagina: {quantidadeEmpresasNaPagina}')
                try:
                    sleep(1.5)
                    empresaZero = navegador.find_elements(By.CLASS_NAME, "hfpxzc")
                    if tipo == 0:
                        for cadaEmpresa in range(quantidadeEmpresasNaPagina):

                            sleep(0.5)
                            empresaZero[cadaEmpresa].click()

                            sleep(1.5)
                            getInfos(fileP)
                            sleep(0.5)

                    else:
                        empresaZero[0].click()
                        sleep(1.5)
                    break
                except (JavascriptException, StaleElementReferenceException, ElementClickInterceptedException) as e:
                    print(e)
                    sleep(1)
            sleep(1.5)



        def modoClicaEmpresa():

            # Aqui ele pega a função desca() e retorna a quantidade de empresas naquela página
            sleep(0.5)
            quantEmpresasNaPagina = desca()

            clicarEmpresas(quantEmpresasNaPagina, 0)

            # getInfos() Código abaixo comentado pois era ele que rodava nas empresas no carrossel...
            '''
            for empresaCrrssl in range(len(empCrrssl)):
                # for empresaCrrssl in range(len(empCrrssl) - 1, len(empCrrssl))
                # for empresaCrrssl in range(len(empCrrssl)):
                sleep(0.5)
                if empresaCrrssl != len(empCrrssl) - 1:
                    focar(empresaCrrssl + 1, navegador)
                else:
                    focar(empresaCrrssl, navegador)
                while True:
                    print("While 2")
                    js = 0
                    try:
                        contadorClickEmpresa = 0

                        while True:
                            print("While 3")
                            contadorClickEmpresa += 1
                            aFoco = navegador.find_elements(By.CLASS_NAME, classEmpresaZero)
                            empCrrssl = navegador.find_elements(By.CLASS_NAME, "Dzbife")
                            if len(empCrrssl) >= 1:
                                try:
                                    if js >= 1:
                                        navegador.execute_script('emps = document.getElementsByClassName("Dzbife")')
                                        navegador.execute_script(f'emps[{empresaCrrssl}].click()')
                                    else:
                                        empCrrssl[empresaCrrssl].click()
                                    break
                                except IndexError as erro:
                                    print(erro)
                                    clicarZeroEmpresa(aFoco)

                            else:
                                navegador.execute_script("window.history.back()")
                                sleep(0.5)
                                # Voltar Uma pagina
                        break
                    except (ElementClickInterceptedException, StaleElementReferenceException) as erro:
                        js += 1
                        print(erro)
                        navegador.execute_script("document.body.style.zoom = 0.8")
                        # pyautogui.press('F12')
                        sleep(1)
                        # pyautogui.press('F12')

                    navegador.execute_script("document.body.style.zoom = 1.0")

                sleep(0.7)'''

        linkAtual = navegador.current_url
        if count != 0:

            for page in range(count):  # Rodar as paginas for page in range(count)
                fecharCard(navegador)
                # navegador.get(linkAtual)
                print(f'PAGINA ATUAL>>>>>>>>> {page}')

                if count != 0:
                    for proximaPag in range(page):  # countZero

                        sleep(2)
                        # navegador.execute_script(f'document.getElementById("ppdPk-Ej1Yeb-LgbsSe-tJiF1e").focus()')

                        px = procuraBtnProx(navegador)
                        if px == 0:
                            break
                        else:
                            bugAceitacao = 0
                            while True:
                                if bugAceitacao == 5:
                                    break
                                try:
                                    px.click()
                                    break
                                except ElementClickInterceptedException:
                                    sleep(2)
                                    bugAceitacao += 1

                pageVaziaAceitacao = 0
                pageVazia = False
                while True:
                    pageVaziaAceitacao += 1
                    if pageVaziaAceitacao == 10:
                        pageVazia = True
                        break
                    try:
                        # a = navegador.find_elements(By.CLASS_NAME, classEmpresaZero)
                        # clicarEmpresas(a, 1)
                        break
                    except:
                        pass
                if pageVazia:
                    continue

                textoPageVazia = navegador.find_elements(By.CLASS_NAME, "qBF1Pd")  # V79n2d-di8rgd-aVTXAb-title
                if len(textoPageVazia) >= 1:
                    pass
                sleep(0.5)
                grausCelsius = navegador.find_elements(By.CLASS_NAME, "mqfAJf-LtZq3b-text")
                cidade = False
                aceitacao = 0
                while True:
                    print("CLS")
                    if aceitacao == 7:
                        print("Não é cidade")
                        break
                    try:
                        if "°C" in grausCelsius[0].text:
                            cidade = True
                        break
                    except IndexError as erro:
                        print(erro)
                        aceitacao += 1
                        pass
                if cidade:
                    while True:
                        print("SGV")
                        try:
                            voltarBtn = navegador.find_elements(By.CLASS_NAME, "xoLGzf-LgbsSe")
                            voltarBtn[0].click()
                            break
                        except IndexError as erro:
                            print(erro)
                            pass
                    sleep(1.5)

                    qep = desca()  # qep: Quantidade de empresas na pagina

                    for e in range(qep):
                        # empresasNaPagina = navegador.find_elements(By.CLASS_NAME, classEmpresaZero)
                        while True:
                            print("KJHÇ")
                            empresasNaPagina = navegador.find_elements(By.CLASS_NAME, classEmpresaZero)
                            try:
                                empresasNaPagina[e].click()
                                break
                            except ElementClickInterceptedException:
                                sleep(0.2)

                        getInfos(fileP)
                        while True:
                            print("SLM")
                            try:
                                voltarBtn = navegador.find_elements(By.CLASS_NAME, "xoLGzf-LgbsSe")
                                voltarBtn[0].click()
                                break
                            except IndexError as erro:
                                print(erro)
                                pass
                else:
                    zoomOut(navegador)
                    modoClicaEmpresa()
                    fecharCard(navegador)
                    navegador.refresh()
                # xoLGzf-LgbsSe botão de voltar CLASSE


        else:
            a = navegador.find_elements(By.CLASS_NAME, classEmpresaZero)
            # clicarEmpresas(a)
            modoClicaEmpresa()
            fecharCard(navegador)
            navegador.refresh()

    if isinstance(cat, list):  # type(categoria) == type(list())
        for catComercio in cat:
            chamar(catComercio, "Supermercados", cid, filePara, nave, catct, ctsing)
    else:
        chamar(cat, loc, cid, filePara, nave, catct, ctsing)


categoria = ''


# Singular pra dar o select nas categorias 12 também conferido
# Singular pra dar o select nas categorias

def escrever(nav, indice, file, categoriasct):
    categoriasS = ['Supermercados', 'Oficinas', 'Restaurante', 'Lanchonete', 'Informática e Eletrônicos',
                   'Eletrodomésticos', 'Vestuário', 'Papelarias', 'Gráficas', 'Serviços de Internet', 'Farmácias',
                   'Hotéis']
    copyCategoriasSing = categoriasS[:]
    nav.get('https://maps.google.com.br/')
    miniMapa(nav)
    if len(categoriasct) != 12:
        categoriasS.clear()
        for item in categoriasct:
            if item in ['Supermercados', 'Mercados']:
                item = ['Supermercados', 'Mercados']
            categoriasS.append(copyCategoriasSing[oldCt.index(item)])
        # categoriasct = ''
    for categoria in categoriasct:
        extrair(categoria, categoria, indice, file, nav, categoriasct, categoriasS)

    # extrair('Farmácias', 'Farmácias', indice, file, nav)
    print(categoriasS)
    print(descartados)
    print(categoriasct)
# Excluir 779 até 830
