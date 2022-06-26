# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from time import sleep
import unicodedata
from selenium.common.exceptions import *

import pyautogui


def fazerlogin(nav):
    # estado = 'Mato Grosso'
    # cidade = 'São José dos Quatro Marcos'
    # chrome_options = Options()
    email = 'atendimento@localizarfacil.com.br'
    senha = 'L8oc*alk@#'
    # navegador = webdriver.Firefox()
    # navegador.maximize_window()
    nav.get("https://dash.localizarfacil.com.br/entrar")

    nav.implicitly_wait(5)
    while True:
        try:
            element_email = nav.find_element(By.NAME, "email")
            element_senha = nav.find_element(By.NAME, "senha")
            btn = nav.find_element(By.CLASS_NAME, "btn")
            break
        except NoSuchElementException:
            nav.delete_all_cookies()
            nav.execute_script("location.reload()")
    nav.implicitly_wait(2)
    element_email.clear()
    element_senha.clear()
    element_email.send_keys(email)
    element_senha.send_keys(senha)
    btn.click()


categoriasSing = ['Supermercados', 'Oficinas', 'Restaurante', 'Lanchonete', 'Informática e Eletrônicos',
                  'Eletrodomésticos', 'Vestuário', 'Papelarias', 'Gráficas', 'Serviços de Internet', 'Farmácias',
                  'Hotéis']

categorias = {
    'Supermercados\n': '66',
    'Oficinas\n': '64',
    'Restaurante\n': '55',
    'Lanchonete\n': '56',
    'Informática e Eletrônicos\n': '67',
    'Eletrodomésticos\n': '77',
    'Vestuário\n': '71',
    'Papelarias\n': '68',
    'Gráficas\n': '69',
    'Serviços de Internet\n': '70',
    'Farmácias\n': '36',
    'Hotéis\n': '74'
}

# Le o arquivo e adiciona as empresas


def escolher_img(tipo, nave):
    sleep(2)
    while True:
        button = nave.find_elements(By.CLASS_NAME, 'btn-options')
        print("OKJHSF")
        try:
            button[6].click()
            break
        except IndexError:
            sleep(0.2)
    sleep(3)
    pyautogui.write(tipo)
    pyautogui.press('enter')
    sleep(0.3)
    pyautogui.moveTo(1335, 445)
    sleep(2)
    button[4].click()
    button[4].click()
    button[5].click()


def adicionar(nav, cidadeSelect, valSelect):
    fazerlogin(nav)

    file = open(f'{cidadeSelect}.txt', 'r', encoding='utf-8')

    content = file.readlines()
    temp = list()
    empresas = list()

    eint = False

    i = len(content) / 6

    if (i - int(i)) == 0 and i > 0:
        i = int(i)
        print(f"Empresas: {i} | Linhas: {i * 6}")
        eint = True

    else:
        print("Arquivo sem linhas ou com linhas não divisíveis por 6")
        print(f"Empresas: {i} | Linhas: {i * 6}")
        nav.close()
    print("==")

    if eint:
        for vez in range(1, i + 1):
            inicio = (6 * vez) - 6
            fim = 6 * vez
            for linhas in range(inicio, fim):  # 6, 12 | 12 - 18
                if linhas != fim - 1:
                    temp.append(content[linhas])
            empresas.append(temp[:])
            temp.clear()

        c1 = ['nome_empresa', 'rua', 'fone', 'categoria', 'palavras_chaves']
        c2 = ['cnpj', 'estrelas', 'estado']
        campos = c1 + c2

        # quantidadeEmpresa = len(empresas)
        for dados in empresas:
            nav.get("https://dash.localizarfacil.com.br/empresa/cadastrar")
            while True:
                try:
                    nav.execute_script('''
                        jdiv = document.getElementsByTagName("jdiv")
                        jdiv[0].remove()''')
                    break
                except JavascriptException:
                    sleep(0.5)

            for item in range(8):
                if campos[item] != 'palavras_chaves':
                    campo_encontrado = nav.find_element(By.ID, campos[item])
                else:
                    campo_encontrado = nav.find_element(By.NAME, campos[item])
                if campos[item] not in ['categoria', 'estado', 'estrelas']:
                    campo_encontrado.clear()

                if item <= 4:
                    if campos[item] != 'fone' and campos[item] != 'categoria':
                        if dados[item] == "0\n":
                                campo_encontrado.send_keys('0')
                        else:
                            try:
                                campo_encontrado.send_keys(dados[item])
                            except WebDriverException:
                                campo_encontrado.send_keys(''.join(c
                                                                   for c in unicodedata.normalize('NFC', dados[item])
                                                                   if c <= '\uFFFF' and c.isascii()))

                    elif campos[item] == 'fone':
                        for n in range(len(dados[item])):
                            if dados[item] == "0\n":
                                campo_encontrado.send_keys('\n')
                            else:
                                campo_encontrado.send_keys(dados[item][n])
                            sleep(0.05)
                    else:  # campos[item] == 'categoria'
                        nav.execute_script("$('#categoria').val(" + categorias[dados[item]] + ")")
                    print(dados[item])

                if campos[item] == 'cnpj':
                    campo_encontrado.send_keys('000')
                elif campos[item] == 'estrelas':
                    nav.execute_script("$('#estrelas').val(1)")
                elif campos[item] == 'estado':  # ESTADO E CIDADE
                    # $("#estado").val(11) 11 = MATO GROSSO
                    nav.execute_script(f'''
                    $("#estado").val(11)
                    var html = '<option selected disabled value="">Selecione...</option>';
                    html += '<option value="{valSelect}">{cidadeSelect}</option>';
                    $('#cidade').html(html).prop('disabled', false);
                    $('#cidade').val({valSelect})
                    ''')

                sleep(0.2)
            nav.execute_script("window.scrollTo(0, 0)")

            btn_dash = nav.find_elements(By.CLASS_NAME, "btn")
            while True:
                try:
                    btn_dash[5].click()
                    break
                except ElementClickInterceptedException:
                    nav.execute_script('''p = document.getElementsByClassName('btn')
                    p[5].focus()''')
                    sleep(0.5)
            nav.implicitly_wait(1)
            escolher_img('logo', nav)
            sleep(3)
            while True:
                try:
                    btn_dash[6].click()
                    break
                except ElementClickInterceptedException as erro:
                    print(erro)
            escolher_img('capa', nav)
            sleep(2)
            nav.execute_script("$('.btn')[9].focus()")
            nav.execute_script("$('.btn')[9].click()")
            sleep(2)
            btn_dash = nav.find_elements(By.CLASS_NAME, "btn")
            while True:
                try:
                    btn_dash[10].click()
                    break
                except ElementClickInterceptedException:
                    nav.execute_script("$('.btn')[9].focus()")
                    nav.execute_script("$('.btn')[9].click()")
            dados.clear()
    nav.close()


def deletar(inicio, fim, nav):
    fazerlogin(nav)
    for identificador in range(inicio, fim + 1):
        nav.get(f'https://dash.localizarfacil.com.br/empresa/{identificador}/excluir')
        sleep(0.4)
    nav.close()


'''
<select data-value="" class="custom-select" name="cidade_id" id="cidade" required="">
<option selected="" disabled="" value="">Selecione...</option>
<option value="1">Mirassol D'Oeste</option>
<option value="2">Cáceres</option>
<option value="3">São José dos Quatro Marcos</option>
<option value="4">Araputanga</option>
<option value="5">Lambari D'Oeste</option>
<option value="6">Cuiabá</option>
<option value="7">Várzea Grande</option>
<option value="8">Pontes e Lacerda</option>
</select>
'''
