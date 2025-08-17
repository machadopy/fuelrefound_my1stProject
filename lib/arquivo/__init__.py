import lib.interface as li

def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro')
    else:
        print(f'Arquivo {nome} criado!')

def lerArq(nome):
    try:
        a = open(nome,'rt')
    except:
        'Erro'
    else:
        li.cabecalho('Tabela de motoristas')
        print(a.read())


def appendtoTab(arq, data_driver):
    a = open(arq, '+at')
    try:
        a.write((f'{data_driver["name"]};{data_driver["lplate"]};{data_driver["drivedis"]};{data_driver["refound"]}'))
    except:
        pass
