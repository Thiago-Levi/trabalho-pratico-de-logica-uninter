# Nome: Thiago Levi Ramos da Costa
# RU: 4335565

# Deve-se codificar uma função dimensoesObjeto (EXIGÊNCIA 1 de 3)
def dimensoesObjeto():

    while True:
        while True:
            # Dentro da função perguntar altura do objeto (em cm);
            # Dentro da função perguntar o comprimento do objeto (em cm);
            # Dentro da função perguntar a largura do objeto (em cm)

            try:
                comprimento = float(input("Digite o comprimento do objeto (em cm): "))
                break
            # Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
            except ValueError:
                print("Valor inválido. --> Digite novamente o comprimento")
                continue

        while True:
            try:
                largura = float(input("Digite a largura do objeto (em cm): "))
                break
            # Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
            except ValueError:
                print("Valor inválido!!! Digite novamente a largura")
                continue

        while True:
            try:
                altura = float(input("Digite a altura do objeto (em cm): "))
                break
            # Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
            except ValueError:
                print("Valor inválido!!! Digite novamente a altura.")
                continue

        # Calcular o volume (em cm) da caixa p/a objeto (altura*largura*comprimento)
        volume = comprimento * largura * altura

        print("O volume do objeto é --> {:.2f} cm³ " .format(volume))

        # Deve-se retornar o valor em (RS) conforme a Quadro 1
        if(volume < 1000):
            valor = 10
            return valor
        elif (volume >= 1000) and (volume < 10000):
            valor = 20
            return valor
        elif (volume >= 10000) and (volume < 30000):
            valor = 30
            return valor
        elif (volume >= 30000) and (volume < 100000):
            valor = 50
            return valor
        else:
            print("Só aceitamos volumes menores de 100000 cm³ --> Entre com dimensões de outro objeto.")

            continue



# Deve-se codificar uma função pesoObjeto (EXIGÊNCIA 2 de 3)
def pesoObjeto():
    while True:
        while True:
            # Dentro da função perguntar peso do objeto (em kg);
            try:
                peso = float(input("Digite o peso do objeto (em Kg): "))
                break
            # Deve-se ter um try/except para o caso de o usuário digitar um valor não numérico;
            except ValueError:
                print("Você digitou um valor não numérico. --> Por favor digite apenas números!")
                continue

        print("O Peso do objeto é: --> Kg {:.2f}" .format(peso))

        multiplicador = 0.0

        # Deve-se retornar o multiplicador conforme o Quadro 2
        # Entendo que a variável peso nõo pode ser <= que dois valores
        # na mesma estrutura condicional.
        # considerei peso < 0.1 e maior que zero

        if(peso > 0.0) and (peso < 0.1):
            multiplicador = 1
            return multiplicador
        elif (peso >= 0.1) and (peso < 1):
            multiplicador = 1.5
            return multiplicador
        elif (peso >= 1) and (peso < 10):
            multiplicador = 2
            return multiplicador
        elif (peso >= 10) and (peso < 30):
            multiplicador = 3
            return multiplicador
        else:
            print("Só aceitamos objetos de menos de 30kg --> Entre com o peso de outro objeto.")
        continue


# Deve-se codificar uma função rotaObjeto (EXIGÊNCIA 3 de 3);
def rotaObjeto():
    # Dentro da função perguntar a rota do objeto desejada
    # (Sugestão: utilize as siglas para facilitar os testes);
    print("Essa são as Rotas que temos:"
          "\n    RS - De Rio de Janeiro até São Paulo "
          "\n    SR - De São Paulo até Rio de Janeiro "
          "\n    BS - De Brasília até São Paulo "
          "\n    SB - De São Paulo até Brasília "
          "\n    BR - De Brasília até Rio de Janeiro "
          "\n    RB - Rio de Janeiro até Brasília")

    while(True):
        rota = input("Digite aqui a SIGLA da rota desejada --> ").lower()
        rotaFoiValidada = (rota == "rs") or (rota == "sr") or (rota == "bs") or (rota == "sb") or (rota == "br") or (rota == "rb")

        # Deve-se retornar o multiplicador conforme o Quadro 3
        multiplicador = 0
        if(rotaFoiValidada):
            if(rota == "rs" or rota == "sr"):
                multiplicador = 1
                return multiplicador
            elif(rota == "bs" or rota == "sb"):
                multiplicador = 1.2
                return multiplicador
            elif (rota == "br" or rota == "rb"):
                multiplicador = 1.5
                return multiplicador
        else:
            print("Você digitou um rota ou um valor inválido -> Digite apenas a sigla da rota desejada")
            continue



##Programa Principal - Main
print("bem-vindo a companhia de logística Thiago Levi S.A")
dimensoes = 0
peso = 0
rota = 0
total = 0
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = dimensoes * peso * rota
print("Total a pagar(R$) --> {:.2f} (dimensões = {:.2f} * peso = {:.2f} * rota = {:.2f})" .format(total, dimensoes, peso, rota))
