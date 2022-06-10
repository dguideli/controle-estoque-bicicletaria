listapecas = []


def cadastrarPeca(cod):
    print('---| CADASTRAR PEÇAS |---')
    print(f'O código da nova peça será: {cod}')
    nome = input('Digite a descrição da peça: ')
    fabricante = input('Digite o nome do fabricante: ')
    preco = input('Digite o valor da peça: ')
    dicionariopeca = {'cod'        : cod,
                      'nome'       : nome,
                      'fabricante' : fabricante,
                      'preco'      : preco}
    listapecas.append(dicionariopeca.copy())


def consultarPeca():
    while True:
        try:
            print('---| CONSULTAR PEÇAS |---')
            print('1 - CONSULTAR TODAS AS PEÇAS')
            print('2 - CONSULTAR PEÇAS POR CÓDIGO')
            print('3 - CONSULTAR PEÇAS POR FABRICANTE')
            print('4 - RETORNAR')
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                print('---| CONSULTAR TODAS AS PEÇAS |---')
                for peca in listapecas:
                    for key, value in peca.items():
                        print(f'{key} : {value}')
            elif opcao == 2:
                print('---| CONSULTAR PEÇAS POR CÓDIGO |---')
                cod_entrada = int(input('Digite o código: '))
                for peca in listapecas:
                    if (peca['cod'] == cod_entrada):
                        for key, value in peca.items():
                            print(f'{key} : {value}')
            elif opcao == 3:
                print('---| CONSULTAR PEÇAS POR FABRICANTE |---')
                cod_entrada = input('Digite o fabricante: ')
                for peca in listapecas:
                    if (peca['fabricante'] == cod_entrada):
                        for key, value in peca.items():
                            print(f'{key} : {value}')
            elif opcao == 4:
                return
            else:
                print('* Digite uma opção válida *')
        except ValueError:
            print('* Você digitou um valor inválido. Tente novamente *')


def removerPeca():
    print('---| REMOVER PEÇAS |---')
    cod_entrada = int(input('Digite o código a ser removido: '))
    for peca in listapecas:
        if (peca['cod'] == cod_entrada):
            listapecas.remove(peca)
            return


# Programa principal
print('Bem vindo ao controle de estoque da Bicicletaria do Diego de Almeida Guideli')
codigopeca = 0
while True:
    try:
        print('1 - CADASTRAR PEÇA')
        print('2 - CONSULTAR PEÇA')
        print('3 - REMOVER PEÇA')
        print('4 - SAIR')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            codigopeca += 1
            cadastrarPeca(codigopeca)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Encerrando o programa!')
            break
        else:
            print('* Digite uma opção válida. *')
    except ValueError:
        print('* Você digitou um valor inválido. Tente novamente *')
