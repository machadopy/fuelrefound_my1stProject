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
        print(f'{'Nome':<10} {'Placa':<10} {'Distancia':<10} {'Reembolso':<10}')
        print(42*'-')
        for line in a:
            data = line.split(';')
            print(f'{data[0]:<10} {data[1]:<10} {data[2]:<10} {int(data[3]):<10.2f}')
        print(42*'-')


def appendtoTab(arq, data_driver):
    a = open(arq, '+at')
    try:
        a.write((f'{data_driver["name"]};{data_driver["lplate"]};{data_driver["drivedis"]};{data_driver["refound"]}\n'))
    except:
        pass
