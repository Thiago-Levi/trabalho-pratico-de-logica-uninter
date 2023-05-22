# Nome: Thiago Levi Ramos da Costa
# RU: 4335565
# Deve-se codificar uma função cadastrarPeca (código) (EXIGÊNCIA 1)
# Essa função recebe como parâmetro um código exclusivo para cada peça cadastrado (DICA: utilize um contador como parâmetro)
def cadastrarPeca(codigoDapeca):
    print("---------- Cadastrar Peça ----------")
    print("Código {}" .format(codigoDapeca))

    # Dentro da função perguntar o nome da peça;
    # Dentro da função perguntar o fabricante da peça;
    # Dentro da função perguntar o valor da peça

    nome = input("Digite o NOME da peca: ")
    fabricante = input("Digite o FABRICANTE da peca: ")
    preco = float(input("Digite o PREÇO(R$) da peca: "))

    # Cada peça cadastrada deve ter os seus dados armazenados num DICIONÁRIO
    dicionarioDePeca = {
        "codigo" : codigo,
        "nome" : nome,
        "fabricante" : fabricante,
        "preco" : preco
    }

    listaDePecas.append(dicionarioDePeca.copy())


# Deve-se codificar uma função consultarPeca(EXIGÊNCIA 2)
def consultarPeca():
    print("---------- Consultar Peça ----------")

    # Dentro da função ter um menu com as seguintes opções:
        # ▪ Consultar Todas as Peças
        # ▪ Consultar Peças por Código
        # ▪ Consultar Peças por Fabricante
        # ▪ Retornar

    while True:
        opcaoConsultarPeca = input("\nEscolha a opção desejada:\n" +
                                   "1 - Consultar TODAS as pecas\n" +
                                   "2 - Consultar pecas por CÓDIGO\n" +
                                   "3 - Consultar peça(s) por FABRICANTE \n" +
                                   "4 - Retornar\n")

        if opcaoConsultarPeca == "1":
            print("Você escolheu a opção consultar TODAS as pecas")
            ## percorre e imprime na tela cada item da lista de dicionários
            for peca in listaDePecas:
                print("-----------------------------------------------")
                for key, value in peca.items():
                    print("{} : {}" .format(key, value))
                print("-----------------------------------------------")

        elif (opcaoConsultarPeca == "2"):
            print("Você escolheu a opção consultar pecas por CÓDIGO")
            codigoDesejado = int(input("Entre com o código desejado: "))
            ## percorre e imprime na tela cada item da lista se o código da peça for o mesmo desejado
            for peca in listaDePecas:
                if peca["codigo"] == codigoDesejado:
                    print("-----------------------------------------------")
                    for key, value in peca.items():
                        print("{} : {}".format(key, value))
                    print("-----------------------------------------------")



        elif (opcaoConsultarPeca == "3"):
            print("Você escolheu a opção consultar peça(s) por FABRICANTE")

            codigoDesejado = input("Entre com o Fabricante: ")
            ## percorre e imprime na tela cada item da lista se o código da peça for o mesmo desejado
            for peca in listaDePecas:
                if peca["fabricante"] == codigoDesejado:
                    print("-----------------------------------------------")
                    for key, value in peca.items():
                        print("{} : {}".format(key, value))
                    print("-----------------------------------------------")

        elif (opcaoConsultarPeca == "4"):
            print("Você escolheu a opção Retornar")
            return

        else:
            print("Opção inválida")
            continue


# Deve-se codificar uma função chamada removerPeca (EXIGÊNCIA 3)
def removerPeca():
    # Dentro da função perguntar qual o código do produto que se deseja remover
    # do cadastro (da lista de dicionário)
    print("---------- Remover Peça ----------")
    codigoDesejado = int(input("Entre com o codigo desejado: "))
    for peca in listaDePecas:
        if peca["codigo"] == codigoDesejado:
            listaDePecas.remove(peca)


# Programa Prncipal Main
print("Bem vindo ao CONTROLE DE ESTOQUE da Bicicletaria do Thiago Levi")

listaDePecas = []
codigo = 0

while True:
    opcaoMenuPrincipal = input("\nEscolha a opção desejada:\n" +
                               "1 - Cadastrar peca\n" +
                               "2 - Consultar peca(s)\n" +
                               "3 - Remover peca \n" +
                               "4 - Sair\n")

    if opcaoMenuPrincipal == "1":
        codigo = codigo + 1
        cadastrarPeca(codigo)

    elif(opcaoMenuPrincipal == "2"):
        consultarPeca()

    elif(opcaoMenuPrincipal == "3"):
        removerPeca()
    elif(opcaoMenuPrincipal == "4"):
        break
    else:
        print("Opção inválida")
        continue
