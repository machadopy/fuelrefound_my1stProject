import lib.arquivo as liA

def line(tam = 42):
    return ('-' * tam)

def cabecalho(txt):
    print(line())
    print(txt.center(42))
    print(line())

def lineV30():
    print('-='*30)

def menu(lista):
    c = 1
    for opc in lista:
        print(f'{c} | {opc}')
        c += 1
    print(line())
    opc = leiaint('Sua opção:')
    return opc


def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('Erro: Digite um numero valido.')
        except(KeyboardInterrupt):
            print('Erro: Programa finalizado.')
            return 0
        else:
            return n
        
def newdriver():
    from math import ceil
    while True:

        driver = dict()


        driver['name'] = str(input('Nome do Colaborador: '))
        driver['lplate'] = str(input('Placa do Veiculo: '))
        driver['startkm'] = int(leiaint('Km Inicio: '))
        driver['finalkm'] = int(leiaint('Km Final: '))
        driver['drivedis'] = driver['finalkm'] - driver['startkm']
        driver['refound'] = driver['drivedis'] / 10 * 7
        driver['refound'] = ceil(driver['refound'])

        return driver

def continuar():
    while True:
        resp = str(input('Quer cadastrar mais motoristas? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda apenas [S/N]: ')
        if resp == 'N':
            print(42*'-')
            break

