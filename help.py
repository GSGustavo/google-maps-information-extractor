class Colors:
    error = '\033[31m'
    end = '\033[0m'


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def sep():
    print('=-' * 20)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def title(value):
    sep()
    print(f'{value:^40}')
    sep()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Erros
def error():
    print(f'{Colors.error}ERRO: Valor Inválido!{Colors.end}')


def error_controlled(value):
    print(f'{Colors.error}{value}{Colors.end}')


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Funções para verificar os 3 tipos de dados que o usuário pode digitar
def verify_str(question):
    while True:
        verify = str(input(question))
        try:
            int(verify)
            error()
        except ValueError:
            break
    return verify


def verify_int(question):
    while True:
        try:
            verify = int(input(question))
            break
        except ValueError:
            error()
    return verify


def verify_float(question):
    while True:
        try:
            verify = float(input(question))
            break
        except ValueError:
            error()
    return verify
# Funções para verificar os 3 tipos de dados que o usuário pode digitar


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Verificando a saida do usuário no loop do main do programa
def verify_quit(question):
    while True:
        try:
            verify = str(input(question)).upper()
            if verify in 'YN':
                break
            else:
                error()
        except ValueError:
            error()
    return verify
# Verificando a saida do usuário no loop do main do programa
