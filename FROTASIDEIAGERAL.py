from time import sleep
import lib.interface as li
import lib.arquivo as liA

arq = 'tabeladriver.txt'
if not liA.arqexiste(arq):
    print('Arquivo nao encontrado')
    liA.criarArquivo(arq)

drivers = list()
driver = dict()
countcod = 0

li.cabecalho('Sistema de Motoristas')

while True:
    resposta = li.menu(['Cadastrar Novo motorista', 'Tabela de motoristas','Encerrar'])
    if resposta == 1:
        li.cabecalho('Cadastro')
        data_driver = li.newdriver()
        liA.appendtoTab(arq, data_driver)      
        print('Cadastro Realizado')
        li.continuar()
        print(42*'-')

    elif resposta == 2:
        liA.lerArq(nome='tabeladriver.txt')

    elif resposta == 3:
        li.cabecalho('Encerrado.')
        break
    sleep(2)