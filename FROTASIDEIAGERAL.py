drivers = list()
driver = dict()
countcod = 0

def line():
    print('-='*30)

line()
print('Sistema de Frotas')
line()

while True:

    driver.clear()

    countcod +=1
    driver['cod'] = countcod
    driver['name'] = str(input('Nome do Colaborador: '))
    driver['lplate'] = str(input('Placa do Veiculo: '))
    driver['startkm'] = int(input('Km Inicio: '))
    driver['finalkm'] = int(input('Km Final: '))
    driver['drivedis'] = driver['finalkm'] - driver['startkm']
    driver['refound'] = driver['drivedis'] / 10 * 7

    drivers.append(driver.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda apenas [S/N]: ')
    if resp == 'N':
        break

line()
print(f'{'REEMBOLSO FROTA':^50}')
line()
print(f'{'COD':^3} {'NOME':>10} {'PLACA':>10} {'DISTANCIA':>10} {'REEMBOLSO R$':>5.10}')
line()

for k, v in enumerate(drivers):
    print(f'{k+1:^3}', end = '')
    print(f'{v["name"]:>10} {v["lplate"]:>10} {v["drivedis"]:>10} {v['refound']:>10.2f}')


'''
for d in drivers:
    print(f'{d["name"]} codigo {d["cod"]} de placa {d["lplate"]}, percorreu {d["drivedis"]}KM, devendo ser reembolsado R${d['refound']:.2f}')'''